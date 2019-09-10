import requests


url = "https://iot.cht.com.tw/iot/v1/device/18341291931/snapshot"
meta = """{
        "id": "ID123",
        "value": ["aaaaa"]
    }"""
# files = "/home/xiec/Aiot/drive-download-20190825T041325Z-001/paradrop.png"
# files = open("/home/xiec/Aiot/drive-download-20190825T041325Z-001/paradrop.png",'rb').read()
# files = {'media': open("/home/xiec/Aiot/drive-download-20190825T041325Z-001/paradrop.png", 'rb')}
files = {
    'file':('paradrop.png',open('/home/xiec/Aiot/drive-download-20190825T041325Z-001/paradrop.png',"rb")),
}
values = {
    'meta': meta,
}
headers = {
    'CK': "PKHTK3E7TX54FEEUHP",
    }

print(type(files))
response = requests.request("POST", url, files=files,data=values,headers=headers)

print(response.text)

# import  os
# with open("/home/xiec/Aiot/drive-download-20190825T041325Z-001/paradrop.png", 'rb') as img:
#   name_img= os.path.basename("/home/xiec/Aiot/drive-download-20190825T041325Z-001/paradrop.png")
#   files= {'image': (name_img,img,'multipart/form-data',{'Expires': '0'}) }
#   with requests.Session() as s:
#     r = s.post(url,files=files,data=values,headers=headers)
#     print(r.status_code)
#     print(r.text)