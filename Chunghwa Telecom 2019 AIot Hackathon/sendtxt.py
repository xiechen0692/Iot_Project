import requests
def send_switch(localtion, x):
    url = "http://iot.cht.com.tw/iot/v1/device/17737013760/rawdata"
    switch_stats = x#'0'
    #payload = "[\r\n    {\r\n        \"id\": \"LB_Lock\",\r\n        \"value\": [\r\n            \"%s\"\r\n        ]\r\n    }\r\n]"%(switch_stats)
    if localtion == 'LB':
        payload = "[\r\n    {\r\n        \"id\": \"LB_Lock\",\r\n        \"value\": [\r\n            \"%s\"\r\n        ]\r\n    }\r\n]"%(switch_stats)
    else:#SB1
        payload = "[\r\n    {\r\n        \"id\": \"RB_Lock\",\r\n        \"value\": [\r\n            \"%s\"\r\n        ]\r\n    }\r\n]"%(switch_stats)
    headers = {'CK': "PKYAHX77YEF0U9ZZ52",}
    response = requests.request("POST", url, data=payload, headers=headers)
    #print(response.text)
#
def send_string(localtion, stryolo):
    url = "http://iot.cht.com.tw/iot/v1/device/17737013760/rawdata"
    # payload = "[\r\n    {\r\n        \"id\": \"LB_Lock\",\r\n        \"value\": [\r\n            \"%s\"\r\n        ]\r\n    }\r\n]"%(switch_stats)
    if localtion == 'LB':
        payload = "[\r\n    {\r\n        \"id\": \"LB_detect_result_string\",\r\n        \"value\": [\r\n            \"%s\"\r\n        ]\r\n    }\r\n]" % (
            stryolo)
    elif localtion == 'SB1':  # SB1
        payload = "[\r\n    {\r\n        \"id\": \"SB1_detect_result_string\",\r\n        \"value\": [\r\n            \"%s\"\r\n        ]\r\n    }\r\n]" % (
            stryolo)
    elif localtion == 'String1':  # SB1
        payload = "[\r\n    {\r\n        \"id\": \"String1\",\r\n        \"value\": [\r\n            \"%s\"\r\n        ]\r\n    }\r\n]" % (
            stryolo)
    headers = {'CK': "PKYAHX77YEF0U9ZZ52", }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)