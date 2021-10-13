import requests

response = requests.get("https://api.github.com/repos/pedro554/funeraria")
print(response.json())