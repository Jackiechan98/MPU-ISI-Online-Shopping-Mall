import urllib
import hashlib
import time
import random
import string
import base64
from urllib.parse import quote
import requests
import json
import os

url = 'http://api.exocr.com/ocr/v1/macau_id_card'
app_key = '6212af43d3e04e73a7a1bf6401d5b727'
app_secret = '3ef0df3476050df644b2ac796fdb4382'
imgfile = 'C:/Users/zqche/Desktop/Final Year Project/test data/test.jpg'
imgurl = 'blob:http://localhost:8080/a3cdbe0b-be86-428c-a831-d979694268cb'
f = base64.b64encode(open(imgfile, 'rb').read())
imgdata = f
params = {
    'app_key' : app_key,
    'app_secret' : app_secret,
    #'image_url' : imgurl,
    'image_base64' : imgdata
}
result_ = requests.post(url, data= params)
string_result = result_.text
result_ = json.loads(string_result)

aa = result_['result']['name']['words']
bb = result_['result']['id']['words']
cc = result_['result']['sex']['words']
dd = result_['result']['birth_date']['words']
ee = result_['description']
ff = result_['error_code']
gg = str(aa) +' '+ str(bb)

print(string_result)
print(aa, bb,cc,dd,ee,ff)
print(gg)