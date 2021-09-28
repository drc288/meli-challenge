from fastapi import APIRouter, Header, Depends, HTTPException
from database.mongodb import AsyncIOMotorClient, get_database
from schemas.ip import IpResponse, IpHomeCheck
from schemas.distance import DistanceResponse
from schemas.position import PositionAvg
from datetime import datetime
from re import search

from config.async_utils import create_new_ip_row, exists_ip, get_ip_data, is_aws, update_ip, csv_log
from config.utils import calculate_distance
from config.distance import verify_distance

api = APIRouter()
regex_validator = r"\b((?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(?:(?<!\.)\b|\.)){4}"


@api.get("/", response_model=IpHomeCheck)
async def home():
    return IpHomeCheck(status=200)


@api.get("/ip/{ip}", response_model=IpResponse)
async def ip_search(ip: str, user_id: str = Header(None), db: AsyncIOMotorClient = Depends(get_database)):
    if not search(regex_validator, str(ip)) or " " in ip:
        raise HTTPException(status_code=400, detail=f"Invalid ip {ip}")

    datetime_now_gmt = datetime.now().strftime("%d/%m/%Y %H:%M:%S GMT")
    await csv_log(user_id=user_id, gmt_time=datetime_now_gmt)
    my_data = await get_ip_data(ip)
    distance = calculate_distance(my_data["country"])
    aws = await is_aws(ip)

    new_row = IpResponse(
        ip=ip,
        fecha_actual=datetime_now_gmt,
        pais=my_data["country"],
        iso_code=my_data["code"],
        distancia_estimada=f"{distance} km",
        pertenece_a_aws=aws
    )
    if (data := await exists_ip(db=db, ip=new_row.ip)) is None:
        await create_new_ip_row(db=db, ip=new_row, distance=distance)
    else:
        await update_ip(db=db, update_ip=data)
    return new_row


@api.get("/farDistance/", response_model=DistanceResponse)
async def ip_far_distance(db: AsyncIOMotorClient = Depends(get_database)):
    elements = []
    cursor = db.IpList.ip.find({}).sort('distancia')
    for doc in await cursor.to_list(length=100):
        elements.append(doc)
    element01 = elements[-1]
    element02 = elements[-2]

    return verify_distance(element01=element01, element02=element02)


@api.get("/closeDistance/", response_model=DistanceResponse)
async def ip_close_distance(db: AsyncIOMotorClient = Depends(get_database)):
    elements = []
    cursor = db.IpList.ip.find({}).sort('distancia')
    for doc in await cursor.to_list(length=100):
        elements.append(doc)
    element = elements[0]
    return_element = DistanceResponse(
        ip=element['ip'],
        pais=element['pais'],
        distancia=element['distancia'],
        invocaciones=element['invocaciones']
    )
    return return_element


@api.get("/avgPosition/{country}", response_model=PositionAvg)
async def avg_position(country: str, db: AsyncIOMotorClient = Depends(get_database)):
    elements = []
    count = 0
    cursor = db.IpList.ip.find({"pais": country.lower()})
    for doc in await cursor.to_list(length=100):
        elements.append(doc)
        count += doc["invocaciones"]
    if len(elements) == 0:
        raise HTTPException(status_code=404, detail=f"country: {country} not found")
    return_element = PositionAvg(
        country=country,
        avg_position=count / len(elements)
    )
    return return_element
