import requests
from datetime import datetime
import os
from pprint import pprint
import json

connection_config = {
    "X-USER-TOKEN": os.environ.get("TOKEN")
}
constants = {
    "pixela_endpoint": "https://pixe.la/v1/users",
    "username": "Allan",
    "token": os.environ.get("TOKEN"),
    "graph_id": "graph1",
    "graph_endpoint": "https://pixe.la/v1/users/sahil/graphs/graph1",
    "graph_config": {
        "id": "graph1",
        "name": "Coding Graph",
        "unit": "hours",
        "type": "float",
        "color": "ajisai"
    },
    "pixel_endpoint": "https://pixe.la/v1/users/sahil/graphs/graph1",
    "pixel_config": {
        "date": datetime.now().strftime("%Y%m%d"),
        "quantity": "2.5"
    },
    "update_endpoint": "https://pixe.la/v1/users/sahil/graphs/graph1/20210701",
    "update_config": {
        "quantity": "3.5"
    },
    "delete_endpoint": "https://pixe.la/v1/users/sahil/graphs/graph1/20210701"
}

connection_response = requests.post(url=constants["pixela_endpoint"], json={
    "token": constants["token"],
    "username": constants["username"],
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}, headers=connection_config)

print(connection_response.text)

graph_response = requests.post(url=constants["graph_endpoint"], json=constants["graph_config"], headers=connection_config)
print(graph_response.text)

pixel_response = requests.post(url=constants["pixel_endpoint"], json=constants["pixel_config"], headers=connection_config)
print(pixel_response.text)

update_response = requests.put(url=constants["update_endpoint"], json=constants["update_config"], headers=connection_config)
print(update_response.text)

delete_response = requests.delete(url=constants["delete_endpoint"], headers=connection_config)
print(delete_response.text)

pprint(json.loads(delete_response.text))

pretty_print = json.dumps(json.loads(delete_response.text), indent=4)
print(pretty_print)
