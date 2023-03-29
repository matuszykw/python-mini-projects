import requests
from datetime import datetime

USERNAME = "matuszykw"
TOKEN = "he2fw879h432709nuf"
GRAPH_ID = "graph1"

#* https://pixe.la/v1/users/matuszykw/graphs/graph1.html

pixela_endpoint = "https://pixe.la/v1/users"

headers = {
    "X-USER-TOKEN": TOKEN,
}


def create_pixel():
    now = datetime.now()
    pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
    hours = input("Enter the number of hours? ")
    pixel_params = {
        "date": now.strftime('%Y%m%d'),
        "quantity": hours,
    }
    response = requests.post(pixel_creation_endpoint, json=pixel_params, headers=headers)
    print(response.text)


def update_pixel():
    date = input("Enter the creation date of pixel(yyyyMMdd): ")
    hours = input("Enter the correct number of hours: ")
    update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"
    update_params = {
        "quantity": hours
    }
    response = requests.put(update_endpoint, json=update_params, headers=headers)
    print(response.text)


def delete_pixel():
    date = input("Enter the creation date of pixel(yyyyMMdd): ")
    delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"
    response = requests.delete(delete_endpoint, headers=headers)
    print(response.text)

print("[1] Create pixel.")
print("[2] Update pixel.")
print("[3] Delete pixel.")
choice = int(input("What do you want to do? "))

if choice == 1:
    create_pixel()
elif choice == 2:
    update_pixel()
elif choice == 3:
    delete_pixel()



#*Creating user
# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

#*Creating graph
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# graph_params = {
#     "id": GRAPH_ID,
#     "name": "Programming Graph",
#     "unit": "Hours",
#     "type": "float",
#     "color": "sora"
# }
# response = requests.post(graph_endpoint, json=graph_params, headers=headers)
# print(response.text)
# print(response.text)