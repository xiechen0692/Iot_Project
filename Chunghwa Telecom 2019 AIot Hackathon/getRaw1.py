import requests
import time
from detect import dection_pic
from sendImage import *
import json
from sendtxt import *

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

# url_LB = "http://iot.cht.com.tw/iot/v1/device/17737013760/sensor/LB_image/snapshot/"
# url_SB1 = "http://iot.cht.com.tw/iot/v1/device/17737013760/sensor/SB1_image/snapshot/"
# url_img = "http://iot.cht.com.tw/iot/v1/device/17737013760/snapshot"
headers_img = {
    'CK': "PKYAHX77YEF0U9ZZ52",
    }

url_yolo = "http://iot.cht.com.tw/iot/v1/device/17737013760/snapshot"

# payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name" \
          # "=\"meta\"\r\n\r\n{\"id\":\"camera\",\"value\":[\"ccc\"]}\r\n" \
          # "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"image\"; filename=\"/home/xiec/Aiot/drive-download-20190825T041325Z-001/q.jpg\"\r\nContent-Type: image/jpeg\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
# payload_yolo = {"file": ('test', open('/home/xiec/Aiot/drive-download-20190825T041325Z-001/img_output/image1.png', "rb"), "image/png"), "meta":(None, json.dumps({"id":"camera","value":["yolo"]}))}
headers_yolo = {
    'CK': "PKYAHX77YEF0U9ZZ52",
    }

previous_key_total = ''#do while
previous_key_LB = ''#do while
previous_key_SB1 = ''#do while
s = 0#flag
while True:
    response = requests.request("GET", url, headers=headers)
    time.sleep(0.5)
    resp_text = json.loads(response.text)
    # resp_text = response.text.split('"')

    now_key_total = resp_text[0]['time']  # substring time
    now_key_LB = resp_text[9]['time']  # substring time
    now_key_SB1 = resp_text[13]['time']#substring time
    # print(resp_text[0]['value'][0].split('//')[1])
    # print(resp_text[0]['value'][1])
    # FOODS = resp_text[-1]['value'][0].split(',')
    # print(FOODS)
    print(now_key_SB1,"++",previous_key_SB1)
    if s == 0:
        previous_key_total = now_key_total
        previous_key_LB = now_key_LB
        previous_key_SB1 = now_key_SB1
        s =+ 1
    if now_key_LB != previous_key_LB and resp_text[9]['value'][1] != 'yolo':#For LB1 yolo
        url_img = "http://iot.cht.com.tw/iot/v1/device/17737013760/sensor/LB_image/snapshot/{}".format(resp_text[9]['value'][0].split('//')[1])#substring key for img
        payload_yolo = {"file": (
        'test', open('/home/xiec/Aiot/drive-download-20190825T041325Z-001/img_output/image1.png', "rb"), "image/png"),
                        "meta": (None, json.dumps({"id": "LB_image", "value": ["yolo"]}))}
        response_img = requests.request("GET", url_img, headers=headers_img)
        if response_img.status_code == 200:
            print("download LBimg")
            with open("img_input/image1.jpg", 'wb') as f:
                f.write(response_img.content)
        object = dection_pic()
        response = requests.request("POST", url_yolo, files=payload_yolo, headers=headers_yolo)#send image
        send_string(localtion = 'LB', stryolo = ','.join(object))
        previous_key_LB = now_key_LB
        print("ok")

    if now_key_SB1 != previous_key_SB1 and resp_text[13]['value'][1] != 'yolo':#For SB1 yolo
        url_img = "http://iot.cht.com.tw/iot/v1/device/17737013760/sensor/SB1_image/snapshot/{}".format(resp_text[13]['value'][0].split('//')[1])#substring key for img
        payload_yolo = {"file": (
        'test', open('/home/xiec/Aiot/drive-download-20190825T041325Z-001/img_output/image1.png', "rb"), "image/png"),
                        "meta": (None, json.dumps({"id": "SB1_image", "value": ["yolo"]}))}
        response_img = requests.request("GET", url_img, headers=headers_img)
        if response_img.status_code == 200:
            print("download SB1img")
            with open("img_input/image1.jpg", 'wb') as f:
                f.write(response_img.content)
        object = dection_pic()
        response = requests.request("POST", url_yolo, files=payload_yolo, headers=headers_yolo)#send image
        send_string(localtion = 'SB1', stryolo = ','.join(object))
        previous_key_SB1 = now_key_SB1
        print("ok")

    if now_key_total != previous_key_total and resp_text[0]['value'][1] != 'yolo':#For SB1 yolo
        url_img = "http://iot.cht.com.tw/iot/v1/device/17737013760/sensor/camera/snapshot/{}".format(resp_text[0]['value'][0].split('//')[1])#substring key for img
        response_img = requests.request("GET", url_img, headers=headers_img)
        if response_img.status_code == 200:
            print("download totalimg")
            with open("img_input/image1.jpg", 'wb') as f:
                f.write(response_img.content)
        object = dection_pic()
        payload_yolo = {"file": (
        'test', open('/home/xiec/Aiot/drive-download-20190825T041325Z-001/img_output/image1.png', "rb"), "image/png"),
                        "meta": (None, json.dumps({"id": "camera", "value": ["yolo"]}))}
        response = requests.request("POST", url_yolo, files=payload_yolo, headers=headers_yolo)#send image
        #send_string(localtion = 'String1', stryolo = ','.join(object))
        previous_key_total = now_key_total
        print("ok")




