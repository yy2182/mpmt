from display import *
import requests
import CONST

def search(name,*args, **kwargs):
    pass

def install(**kwargs):
    if kwargs["name"] == "jei" : 
        print("下载开始")
        with open("./mods/jei.jar","wb") as f:
            f.write(requests.get(CONST.JEI_URL).content)
        print("下载结束")

def configure():
    pass
