import requests
from dotenv import load_dotenv
import os
load_dotenv()


SERVICE_B_URL = os.getenv("SERVICE_B_URL")
IP_API_URL = "http://ip-api.com/json/"


def get_coordinates(ip: str):
    response = requests.get(f"http://ip-api.com/json/{ip}?fields=lat,lon,query")
    data = response.json()
    return data


def send_to_service_b(coordinates: dict):
    response = requests.post(
        f"{SERVICE_B_URL}/coordinates/add_location",
        json=coordinates)


    if not response.ok:
        raise Exception("failed to send data to service B")

    return coordinates

def resolve_ip_and_send(ip):
    coordinates = get_coordinates(ip)
    data = send_to_service_b(coordinates)
    return data


