from app.schemas.distance import DistanceResponse


def verify_distance(element01: dict, element02: dict):
    """
    validate the distance and the invocationes in database
    :param element01: last element
    :param element02: before the last element
    :return: the element with many invocation and great distance
    """
    if element01['pais'] == element02['pais']:
        if element01["invocaciones"] > element02["invocaciones"]:
            return_element = DistanceResponse(
                ip=element01['ip'],
                pais=element01['pais'],
                distancia=element01['distancia'],
                invocaciones=element01['invocaciones']
            )
        else:
            return_element = DistanceResponse(
                ip=element02['ip'],
                pais=element02['pais'],
                distancia=element02['distancia'],
                invocaciones=element02['invocaciones']
            )
    else:
        return_element = DistanceResponse(
            ip=element01['ip'],
            pais=element01['pais'],
            distancia=element01['distancia'],
            invocaciones=element01['invocaciones']
        )

    return return_element
