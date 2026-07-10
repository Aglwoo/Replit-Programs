import requests

version = input("Version Number: ")
if version == "1.20.5":
    url = "https://api.papermc.io/v2/projects/paper/versions/1.20.5/builds/22/downloads/paper-1.20.5-22.jar"
    r = requests.get(url, allow_redirects=True)
    open('paper-1.20.5-22.jar', 'wb').write(r.content)