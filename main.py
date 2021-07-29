import requests
from datetime import datetime

USERNAME = "mengchien"
TOKEN = "weqe124dseqw"
pixela_endpoint = "https://pixe.la/v1/users"
GRAPH_ID = "graph1"

user_params = {
    "token":TOKEN ,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

header = {
    "X-USER-TOKEN": TOKEN
}

today = datetime(year=2021, month=7, day=22)
today = today.strftime("%Y%m%d")
pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
response_ = requests.delete(url=pixel_delete_endpoint,  headers=header)
print(response_.text)
print(pixel_delete_endpoint)