import requests
import json
url = "http://iot.cht.com.tw/iot/v1/device/17737013760/snapshot"

# payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name" \
          # "=\"meta\"\r\n\r\n{\"id\":\"camera\",\"value\":[\"ccc\"]}\r\n" \
          # "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"image\"; filename=\"/home/xiec/Aiot/drive-download-20190825T041325Z-001/q.jpg\"\r\nContent-Type: image/jpeg\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
# payload = {"file": ('test', open('/home/xiec/Aiot/drive-download-20190825T041325Z-001/img_output/image1.png', "rb"), "image/png"), "meta":(None, json.dumps({"id":"camera","value":["ccc"]}))}


headers = {
    'CK': "PKYAHX77YEF0U9ZZ52",
    'User-Agent': "PostmanRuntime/7.15.2",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "f62a05be-3e07-4a4c-a5d0-1825805c3ba4,1a896e78-5c75-45c8-b8ba-68ec3f1819ac",
    'Host': "iot.cht.com.tw",
    'Accept-Encoding': "gzip, deflate",
    'Content-Length': "38630",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }
def upload():
    response = requests.request("POST", url, files=payload, headers=headers)
    print(response.text)

#upload()