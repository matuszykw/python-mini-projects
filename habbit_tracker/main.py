import requests
from datetime import datetime

USERNAME = "matuszykw"
TOKEN = "he2fw879h432709nuf"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
#*Creating user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": GRAPH_ID,
    "name": "Programming Graph",
    "unit": "Hours",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN,
}
#*Creating graph
# response = requests.post(graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

#*Creating pixel
now = datetime.now()
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_params = {
    "date": now.strftime('%Y%m%d'),
    "quantity": "1.5",
}
# response = requests.post(pixel_creation_endpoint, json=pixel_params, headers=headers)
# print(response.text)

#*Updating pixel data
update_date = datetime(2023, 3, 25)
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{update_date.strftime('%Y%m%d')}"
update_params = {
    "quantity": "0"
}
# response = requests.put(update_endpoint, json=update_params, headers=headers)
# print(response.text)

#*Deleting pixel data
delete_date = datetime(2023, 5, 23)
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{delete_date.strftime('%Y%m%d')}"
# response = requests.delete(delete_endpoint, headers=headers)
# print(response.text)