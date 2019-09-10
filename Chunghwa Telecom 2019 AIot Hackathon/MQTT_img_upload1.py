import requests
import json

url = "http://iot.cht.com.tw/iot/v1/device/17737013760/snapshot"

files = {"file": ('test', open('/home/xiec/Aiot/drive-download-20190825T041325Z-001/q.jpg', "rb"), "image/jpeg"), "meta":(None, json.dumps({"id":"camera","value":["ccc"]}))}

headers = {
    'CK': "PKYAHX77YEF0U9ZZ52"
    }

response = requests.request("POST", url, files=files,headers=headers)

print(response.text)