import requests
from datetime import datetime


today = datetime.now()

USERNAME = "anjesh"
graph_id = "graph1"


pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token" : "**************",
    "username" : "anjesh",
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}
# response = requests.post(url= pixela_endpoint, json=user_params)


graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN" : "***************"
}

graph_params = {
    "id" : "graph1",
    "name" : "Cycling Graph",
    "unit" : "km",
    "type" : "float",
    "color" : "ajisai"
}

# graph_response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)

post_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{graph_id}"

post_params = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : "50.0"
}

# post_response = requests.post(url=post_endpoint, json=post_params, headers=headers)

put_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{graph_id}/{today.strftime('%Y%m%d')}"

put_params = {
    "quantity" : "10.0"
}

# put_response = requests.put(url=put_endpoint, json=put_params, headers=headers)

delete_endpoint = put_endpoint

delete_response = requests.delete(url=delete_endpoint, headers=headers)

print(delete_response.text)