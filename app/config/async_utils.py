from ..database.mongodb import AsyncIOMotorClient
from ..schemas.ip import IpResponse
from ipaddress import ip_address, ip_network
from aiocsv import AsyncWriter

import httpx
import aiofiles


async def exists_ip(db: AsyncIOMotorClient, ip: str):
    """
    Verify if exists the ip in database
    :param db: db connection
    :param ip: ip to verify
    :return: None if not exists or de schema if exists
    """
    if (result := await db.IpList.ip.find_one({"ip": ip})) is not None:
        return result
    else:
        return None


async def create_new_ip_row(db: AsyncIOMotorClient, ip: IpResponse, distance: int):
    """
    Create new row in database
    :param distance: ditance in integer
    :param db: db connection
    :param ip: ip to integrate
    :return: The schema
    """
    document = {
        "ip": ip.ip,
        "pais": ip.pais,
        "distancia": distance,
        "invocaciones": 1
    }
    await db.IpList.ip.insert_one(document)


async def get_ip_data(ip: str):
    """
    Get country name and country code
    :param ip: ip to search
    :return: object with country and code
    """
    url = f"https://api.ip2country.info/ip?{ip}"
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()
        data = resp.json()

        return_obj = {
            "country": str(data.get('countryName')).lower(),
            "code": str(data.get('countryCode')).lower()
        }

    return return_obj


async def is_aws(ip: str):
    """
    Verify if ip are in network
    :param ip: ip to search
    :return: True if ip are in network or False if not
    """
    url = "https://ip-ranges.amazonaws.com/ip-ranges.json"
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()
        data = resp.json()

        ip_detail_cloud = data.get("prefixes")

    for item in ip_detail_cloud:
        address = ip_address(ip)
        network = ip_network(item["ip_prefix"])

        if address in network and item["service"] == "AMAZON":
            return True
    return False


async def update_ip(db: AsyncIOMotorClient, update_ip: dict):
    """
    Update invocaciones
    :param db: db connection
    :param update_ip: object to update data
    :return: schema
    """
    _id = update_ip["_id"]
    update_ip["invocaciones"] += 1
    await db.IpList.ip.replace_one({'_id': _id}, update_ip)


async def csv_log(user_id: str, gmt_time: str):
    """
    Async csv writer file
    :param user_id: the user id
    :param gmt_time: gmt datetime now
    :return: None
    """
    async with aiofiles.open("log.csv", mode="a", encoding="utf-8") as afp:
        write = AsyncWriter(afp, dialect="unix")
        await write.writerow([gmt_time, user_id])
