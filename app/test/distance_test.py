from app.config.distance import verify_distance

element01 = {
    "ip": "9.9.9.9",
    "pais": "france",
    "distancia": 11859,
    "invocaciones": 10,
    "pertenece_a_aws": False
}

element02 = {
    "ip": "9.9.9.9",
    "pais": "france",
    "distancia": 10859,
    "invocaciones": 10,
    "pertenece_a_aws": False
}


def test_distance():
    obj_to_return = verify_distance(element01, element02)
    print(obj_to_return)
    assert obj_to_return == element01


if __name__ == "__main__":
    test_distance()