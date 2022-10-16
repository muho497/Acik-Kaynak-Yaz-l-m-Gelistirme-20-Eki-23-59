import requests

URL ="https://api.spacexdata.com/v5/launches/latest"


result = requests.get(URL)

data = result.json()

print(data)