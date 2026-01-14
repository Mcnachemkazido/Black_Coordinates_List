import requests


SERVICE_B_URL = "http://localhost:8000"
IP_API_URL = "http://ip-api.com/json/"


def get_coordinates(ip: str):
    response = requests.get(f"http://ip-api.com/json/{ip}?fields=lat,lon,ip,query")
    data = response.json()
    return data


def send_to_service_b(coordinates: dict):
    response = requests.post(
        f"{SERVICE_B_URL}/coordinates/add_location",
        json=coordinates)


    if not response.ok:
        raise Exception("failed to send data to service B")

    return coordinates

def resolve_ip_and_send(ip: str):
    coordinates = get_coordinates(ip)
    data = send_to_service_b(coordinates)
    return data


