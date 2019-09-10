import requests
import time
from detect import dection_pic
from sendImage import *
import json

url = "http://iot.cht.com.tw/iot/v1/device/17737013760/rawdata"
headers = {
    'CK': "PKYAHX77YEF0U9ZZ52",
    'User-Agent': "PostmanRuntime/7.15.2",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "d5022e03-d0db-453b-aeae-e5356a75cc42,7f32a980-79a4-498e-bd75-d5b856c43972",
    'Host': "iot.cht.com.tw",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

# url_img = "http://iot.cht.com.tw/iot/v1/device/17737013760/rawdata"
headers_img = {
    'CK': "PKYAHX77YEF0U9ZZ52",
    'User-Agent': "PostmanRuntime/7.15.2",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "0aa34f8d-8d07-4a89-8997-ac83033b6a66,796d91c4-3005-4731-b0da-dd5d60387b3b",
    'Host': "iot.cht.com.tw",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

previous_key = ''
s = 0

while True:
    response = requests.request("GET", url, headers=headers)
    time.sleep(0.5)
    resp_text = response.text.split('"')
    now_key = resp_text[-4]#substring time
    print(resp_text[-4])
    if s == 0:
        previous_key = now_key
        s =+ 1
    if now_key != previous_key:
        print("download img")
        url_img = "http://iot.cht.com.tw/iot/v1/device/17737013760/sensor/camera/snapshot/{}".format(now_key[11:])#substring key for img
        response_img = requests.request("GET", url_img, headers=headers_img)
        if response_img.status_code == 200:
            with open("img_input/image1.jpg", 'wb') as f:
                f.write(response_img.content)
        dection_pic()
        time.sleep(1.5)
        upload()
        previous_key = now_key




