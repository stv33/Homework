import requests
from bs4 import BeautifulSoup
import os
import json
import base64
import cv2

class Face():
    def __init__(self,score,x,y,row,col):
        self.score=score
        self.x = x
        self.y = y
        self.row = row
        self.col = col
    
    def get_judgement(self):
        if self.score >= 60:
            return "S"
        elif self.score >= 50:
            return "A+"
        elif self.score >= 40:
            return "A"
        else:
            return "A-" 

class judging(object):


    def access_token_fuc(self):

        api_key = '7kKDWk30B4oe5Hs0NM3zcAst'
        secret_key = '24tFjDMmdnfxTj8h0Rcx6jrLaoDul4S6'
        url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + str(api_key) + '&client_secret=' + str(secret_key)
        res = eval(requests.get(url).text)
        self.access_token=res['access_token']
        self.header = {
            'Content-Type':'application/json'
        }
        self.data={
             "image_type":"BASE64",
             "face_field":"beauty",
        }
        self.face_text = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
        self.face_text = self.face_text +"?access_token="+self.access_token

    def API_judgement(self):
    #将拍下的照片发送给百度
        with open('image.jpg','rb') as f:
            image = base64.b64encode(f.read())
            self.data["image"]=str(image,'utf-8')

        res2= eval(requests.post(url=self.face_text,data=self.data,headers=self.header).text)

        #获取人脸位置和颜值信息

        Answer=Face(int(res2["result"]["face_list"][0]["beauty"]),
        int(res2["result"]["face_list"][0]["location"]["left"]),
        int(res2["result"]["face_list"][0]["location"]["top"]),
        int(res2["result"]["face_list"][0]["location"]["width"]),
        int(res2["result"]["face_list"][0]["location"]["height"]))
        print("颜值：",Answer.score)
        print("x:",Answer.x,"y:",Answer.y,"x+row:",Answer.x+Answer.row,"y+col:",Answer.y+Answer.col)
        #给保存好的图片加上框框和备注
        img_token=cv2.imread("image.jpg")
        colors = (0,0,255)
        cv2.rectangle(img_token, (Answer.x, Answer.y), (Answer.x+Answer.row,Answer.y+Answer.col), colors, 5)
        cv2.putText(img_token, Answer.get_judgement(), (Answer.x,Answer.y), cv2.FONT_HERSHEY_SIMPLEX, 5, colors, 12)
        cv2.imwrite("imageWithjudgement.jpg",img_token)




