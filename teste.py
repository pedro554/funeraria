import requests

response = requests.get("https://api.github.com/repos/v2ray/v2ray-core/releases/latest")
print(response.json()["name"])