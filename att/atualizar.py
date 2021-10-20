import git
import os
import requests
import json
import sys
import shutil


path = os.path.dirname(__file__)
path = path.split('\\')
path.pop(-1)
a = ''
for x in path:
    a += x + '\\'

response = requests.get("https://api.github.com/repos/pedro554/funeraria/tags")
current_version = response.json()[0]['name']
data = {"version": current_version}


dir_path = f'{a}\\funeraria'

try:
    shutil.rmtree(dir_path)
except OSError as e:
    print("Error: %s : %s" % (dir_path, e.strerror))


git.Git(path).clone('https://github.com/pedro554/funeraria.git')
with open(f"{a}\\version.json", 'w') as f:
    json.dump(data, f)