import ctypes
import json
import os
import shutil
import subprocess
import tkinter
from subprocess import Popen
from tkinter import messagebox

import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView


def makefolder(folder):
    if not(os.path.isdir(folder)):
        os.makedirs(os.path.join(folder))
        return 0
    else:
        return 1   
def delfolder(folder):
    if os.path.isdir(folder):
        shutil.rmtree(folder)
def check():
    URL = 'https://gametowndev.tk/list.json'
    response = requests.get(URL)
    modpacklist = response.json()
    return modpacklist["modpack"]
def login(ID, password):
    auth = {"agent": {"name": "Minecraft", "version":1},"username":ID,"password":password,"requestUser":True}
    data = json.dumps(auth)
    url = "https://authserver.mojang.com/authenticate"
    response = requests.post(url=url, data=data)
    if response.status_code == 200 or response.status_code == 403:
        res = response.json()
        if 'error' in res.keys():
            return 1,res['error'], res['errorMessage']
        else:
            return 0,res['selectedProfile']['name'],res["selectedProfile"]["id"],res['accessToken'],res['clientToken']
    else:
        return 2,response.status_code
def download(url,folder):
    subprocess.call(["./wget.exe", "-P {} {}".format(folder, url)])
def downloadfolder(url,folder):
    subprocess.call(["./wget.exe", "-r -P {} {}".format(folder, url)])
def launch(modpack,jvm):
    with open("./instance/{}/timestamp.json".format(modpack)) as f:
        data = json.load(f)
    with open("./instance/jvm.txt", 'w') as f:
        f.write(jvm)
    print("실행")
    print(modpack)
    url = "https://gametowndev.tk/{}.json".format(modpack)
    response = requests.get(url)
    packdata = response.json()
    time = "https://gametowndev.tk/{}/timestamp.json".format(modpack)
    timestamp = requests.get(time).json()['timestamp']
    print(packdata['version'])
    if timestamp > data['timestamp']:
        update(modpack,packdata)
    path = os.environ['cd']
    ctypes.windll.shell32.ShellExecute(0,'open',path + "/java/bin/java.exe")
    
def update(modpack, packdata):
    update = packdata['update']
    folder="./instance/{}".format(modpack)
    makefolder(folder)
    for i in update:
        delfolder(folder + "/" + i)
    downloadfolder("https://gametowndev.tk/{}".format(modpack), "./instance/{}".format(modpack))
def launchwrapper(self, obj1, obj2, obj3, obj4):
    id=obj1.text()
    password=obj2.text()
    root = tkinter.Tk()
    root.withdraw()
    
    data = login(id,password)
    if data[0] == 1:
        messagebox.showerror("Error","{} : \n{}".format(data[1],data[2]))
    elif data[0] == 2:
        root = tkinter.Tk()
        root.withdraw()
        messagebox.showerror("Error","Http 통신에러\n서버 응답코드 {}".format(data[1]))
    else:
        launch(obj3.currentItem().text(),obj4.toPlainText())
    print("실행 워래퍼")
    print(data)
