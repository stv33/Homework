import requests
from bs4 import BeautifulSoup
import os
import json
import base64
import cv2



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
#拍照功能实现
cap = cv2.VideoCapture(0)
while True:
    sucess,img =cap.read()
    cv2.imshow("img",img)
    k=cv2.waitKey(1)
    if k ==27:
        cv2.destoryAllwindow()
        break
    elif k==ord("s"):
        cv2.imwrite("image.jpg",img)

        break
cap.release()
#将拍下的照片发送给百度
with open('image.jpg','rb') as f:
    image = base64.b64encode(f.read())
    data["image"]=str(image,'utf-8')

res2= eval(requests.post(url=face_text,data=data,headers=header).text)

#获取人脸位置和颜值信息
score=int(res2["result"]["face_list"][0]["beauty"])
x=int(res2["result"]["face_list"][0]["location"]["left"])
y=int(res2["result"]["face_list"][0]["location"]["top"])
row=int(res2["result"]["face_list"][0]["location"]["width"])
col=int(res2["result"]["face_list"][0]["location"]["height"])
print("颜值：",score)
print("x:",x,"y:",y,"x+row:",x+row,"y+col:",y+col)
#给保存好的图片加上框框和备注
img_token=cv2.imread("image.jpg")
colors = (0,0,255)
cv2.rectangle(img_token, (x, y), (x+row,y+col), colors, 5)
cv2.imshow("img",img_token)
cv2.waitKey()



