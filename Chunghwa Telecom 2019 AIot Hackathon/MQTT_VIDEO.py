import requests

url = "https://iot.cht.com.tw/apis/CHTIoT/ivs-tw/v1/video"
meta = """{
        "direction": 0,
        "x1": 200,
        "y1": 10,
        "x2": 200,
        "y2": 1000
    }"""
files = {
    # 'file':('people.mp4',open("C:\\Users\\Vensen\\Desktop\\Apps\\CHT_AIOT\\people.mp4","rb"))
    'file':('paradrop.png',open('/home/xiec/Aiot/drive-download-20190825T041325Z-001/paradrop.png',"rb")),
}
values = {
    'meta':meta
}
headers = {
    'X-API-KEY': "ab2a5cda-2209-4473-b82c-e55459ea3c0c",
    'cache-control':"no-cache",
    }

response = requests.request("POST", url, files=files,data=values,headers=headers,timeout=3000)

print(response.text)