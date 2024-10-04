import requests
from datetime import datetime

TOKEN = "dgsfgnzgnsbdgnjkdafjhgkjbdsdbfvsdijokjfbjdf"
USERNAME = "mohamedhamdy"
pixela_endpoint = " https://pixe.la/v1/users"
user_params = {"token": TOKEN,
               "username": USERNAME,
               "agreeTermsOfService": "yes",
               "notMinor": "yes"
               }

# response = requests.post(url=pixela_endpoint, json=user_parames)
# print(response.text)
today = datetime.now()
today_in_format = today.strftime("%Y%m%d")
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params = {
    "id": "graph1",
    "name": "GEM",
    "unit": "hours",
    "type": "float",
    "color": "momiji"
}
headers = {
    "X-USER-TOKEN": TOKEN

}
# response = requests.post(url=graph_endpoint,json= graph_params,headers=headers)
# print(response.text)
pixel_endpoint = f"{graph_endpoint}/graph1"
pixel_params = {
    "date": today_in_format,
    "quantity": "3"
}

update_endpoint = f"{pixel_endpoint}/{today_in_format}"
update_params = {
    "quantity": "4"
}
response = requests.delete(url=update_endpoint, headers=headers)
print(response.text)
