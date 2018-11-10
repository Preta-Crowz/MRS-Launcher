import os
import requests
import json
def login(ID, password):
    auth = {"agent": {"name": "Minecraft", "version":1},"username":ID,"password":password,"requestUser":True}
    data = json.dumps(auth)
    url = "https://authserver.mojang.com/authenticate"
    response = requests.post(url=url, data=data)
    if response.status_code == 200:
        res = responce.json()
        if 'error' in res.keys():
            return 1,res['error'], res['errorMessage']
        else:
            return 0,res['selectedProfile']['name'],res["selectedProfile"]["id"],res['accessToken'],res['clientToken']
    else:
        return 2,response.status_code
'''def launch(name,version,uuid,token):
    subprocess.check_output(['cmd', '/c echo 에휴'],universal_newlines=True)'''