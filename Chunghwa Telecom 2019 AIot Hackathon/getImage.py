import requests
import PIL
from PIL import Image

url = "http://iot.cht.com.tw/iot/v1/device/17737013760/sensor/camera/snapshot/1b9042f8-2056-4067-9a85-9fcf834b5706"

headers = {
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

response = requests.request("GET", url, headers=headers)
# response.encoding = None
# # response.apparent_encoding = 'ISO-8859-1'
# print('encoding:', response.encoding)
# # response的网页头部的编码
# print('apparent_encoding:', response.apparent_encoding)
# print(response.text)
# print(response.headers)
if response.status_code == 200:
    with open("image1.jpg", 'wb') as f:
        f.write(response.content)
