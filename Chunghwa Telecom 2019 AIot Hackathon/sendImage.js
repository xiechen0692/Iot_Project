var fileData = this.files[0],
    myData = new FormData();
myData.append("meta", "{\"id\":\"camera\",\"value\":[\"ccc\"]}");
myData.append("image", "/C:/Users/Think/Pictures/q.jpg");

var settings = {
  "async": true,
  "crossDomain": true,
  "url": "http://iot.cht.com.tw/iot/v1/device/17737013760/snapshot",
  "method": "POST",
  "headers": {
    "CK": "PKYAHX77YEF0U9ZZ52",
    "Content-Type": "application/json",
    "User-Agent": "PostmanRuntime/7.15.2",
    "Accept": "*/*",
    "Cache-Control": "no-cache",
    "Postman-Token": "4e049f6f-1cdd-4e9f-81b1-559a61be5865,8dcf042c-a908-47c7-ad99-9ef0b3d563d0",
    "Host": "iot.cht.com.tw",
    "Accept-Encoding": "gzip, deflate",
    "Content-Length": "31522",
    "Connection": "keep-alive",
    "cache-control": "no-cache"
  },
  "processData": false,
  "contentType": false,
  "mimeType": "multipart/form-data",
  "data": form
}

$.ajax(settings).done(function (response) {
  console.log(response);
});