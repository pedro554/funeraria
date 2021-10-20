import requests
import json

def check(file, path):
    response = requests.get("https://api.github.com/repos/pedro554/funeraria/tags")
    current_version = response.json()[0]['name']
    print(current_version)

    f = open(file, 'r')

    data = json.load(f)

    if data['version'] != current_version:
        return False
    else:
        return True