import requests
from bs4 import BeautifulSoup
import os
import json
import base64

api_key = '7kKDWk30B4oe5Hs0NM3zcAst'
secret_key = '24tFjDMmdnfxTj8h0Rcx6jrLaoDul4S6'
url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + str(api_key) + '&client_secret=' + str(secret_key)
res = eval(requests.get(url).text)
access_token=res['access_token']
face_text = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
face_text = face_text +"?access_token="+access_token
header = {
    'Content-Type':'application/json'
}
data={
    "image_type":"BASE64",
    "face_field":"beauty",
}
with open('1234.jpg','rb') as f:
    image = base64.b64encode(f.read())
    data["image"]=str(image,'utf-8')

res2= eval(requests.post(url=face_text,data=data,headers=header).text)

print("颜值：",res2["result"]["face_list"][0]["beauty"])

    

