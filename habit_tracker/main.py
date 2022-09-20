import requests
from datetime import datetime


USERNAME = "quincy"
TOKEN = "me5PC6m611nSqiLGrPs!tdySt"
GRAPH_ID = "graph01"

# 1 Create your user account (Pixela)
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


# 2 Create a graph definition
graph_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Workout Graph",
    "unit": "minutes",
    "type": "int",
    "color": "momiji",
}
request_header = {
    "X-USER-TOKEN": TOKEN,
}
# graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(graph_response.text)


# 3 Post a pixel
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
pixel_data = {
    "date": today.strftime('%Y%m%d'),
    "quantity": input("How many minutes did you workout for today?: "),
}
pixel_response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=request_header)
print(pixel_response.text)


# 4 Update a pixel
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
pixel_update_data = {
    "quantity": "30",
}
# update_response = requests.put(url=update_endpoint, json=pixel_update_data, headers=request_header)
# print(update_response.text)



# 5 Delete a pixel
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# delete_response = requests.delete(url=delete_endpoint, headers=request_header)
# print(delete_response.text)