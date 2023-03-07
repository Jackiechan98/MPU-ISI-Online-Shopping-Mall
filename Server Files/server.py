from flask import Flask
from flask import request, jsonify
from flask_cors import CORS #解决跨域问题
import hashlib #encrypt
import json
import pymysql #interactive with mysql
import mysql
from mysql import is_number, check_number_exist, check_letter_exist, check_total

import urllib
import time
import random
import string
import base64
from urllib.parse import quote
import requests
import os

app=Flask(__name__) #创建程序实例
cors=CORS(app) #解决跨域问题

# @app.after_request
# def cors(environ):
#     environ.headers['Access-Control-Allow-Origin']='*'
#     environ.headers['Access-Control-Allow-Method']='*'
#     environ.headers['Access-Control-Allow-Headers']='x-requested-with,content-type'
#     return environ

@app.route("/")
def index():
    return '<h1>This is a final year project of Jacky.</h1>'

@app.route('/hello', defaults={'name': 'Wilson'})
@app.route("/hello/<name>")
def say_hello(name):
    return '<h1>Hello, %s!</h1>' % name


@app.route("/index")
def get_indexgoods():
    result=mysql.doIt("select uid from user")
    return json.dumps(result)

@app.route("/user/login",methods=["POST"])
def login():
    #Get user ID and password
    userid=request.json.get("userid")
    password=request.json.get("password")
    #Encryption
    password=hashlib.sha1(password.encode()).hexdigest()
    #Query database
    result=mysql.doIt("SELECT * FROM user where uid='"+userid+"' and `password`='"+password+"'")
    #Get the results
    returnmsg={"status":0,'desc':"login successfully","uid":userid,"data":result}
    if(len(result)==0):
        returnmsg["status"]=1
        returnmsg["desc"]="Wrong password or useid"
        returnmsg["uid"]=0
    else:
        returnmsg["uid"]=userid
        returnmsg["info"]=result[0]
    return json.dumps(returnmsg)

@app.route("/user/register",methods=["POST"])
def register():
    userid=request.json.get("userid")
    username=request.json.get("username")
    password=request.json.get("password")
    email=request.json.get("email")
    address=request.json.get("address")
    returnmsg={"status":0,'desc':"Register success","uid":userid}
    if all([userid,username,password,email,address]):
        password=hashlib.sha1(password.encode()).hexdigest()
        mysql.commit("INSERT INTO user(uid, \
        password,uName,uAddress,email) \
        VALUES ('%s', '%s', '%s', '%s', '%s')" % \
        (userid, password,username,address,email))
        returnmsg={"status":0,'desc':"Register success","uid":userid,"password":password,
            "uName":username,"email":email,"uAddress":address}
        
    else:
        returnmsg["status"]=1
        returnmsg["desc"]="Incomplete register form"
        returnmsg["uid"]=0
    return json.dumps(returnmsg)

@app.route("/user/changepw",methods=["POST"])
def changepw():
    #Get userid and pw
    userid=request.json.get("userid")
    oldpassword=request.json.get("oldpassword")
    newpassword=request.json.get("newpassword")
    returnmsg={"status":0,'desc':"Change password success","uid":userid}

    if all([userid,oldpassword,newpassword]):

        oldpassword=hashlib.sha1(oldpassword.encode()).hexdigest()

        result=mysql.doIt("SELECT * FROM user where uid='"+userid+"' and `password`='"+oldpassword+"'")
        if(len(result)!=0):
            if check_total(newpassword):
                newpassword=hashlib.sha1(newpassword.encode()).hexdigest()
                mysql.commit("UPDATE user SET password='"+newpassword+"' where uid='"+userid+"'")
                returnmsg["status"]=0
                returnmsg["desc"]="You have successfully change your password!"
                returnmsg["uid"]=userid
                returnmsg={"status":0,'desc':"Change password success","uid":userid}

            else: 
                returnmsg["status"]=1
                returnmsg["desc"]="The password should contain at least 6 characters, in which there must be at least one digit and one capital letter."
                returnmsg["uid"]=0
        else:
            returnmsg["status"]=1
            returnmsg["desc"]="Wrong password or useid"
            returnmsg["uid"]=0 
    else:
        returnmsg["status"]=1
        returnmsg["desc"]="Wrong password or useid"
        returnmsg["uid"]=0
    return json.dumps(returnmsg)



@app.route("/users/my")
def get_order_status():
    id=request.args.get("id")
    returnmsg={}
    return returnmsg

@app.route("/user/register/recognize")
def img_recognize_result():
    url = 'http://api.exocr.com/ocr/v1/macau_id_card'
    app_key = '6212af43d3e04e73a7a1bf6401d5b727'
    app_secret = '3ef0df3476050df644b2ac796fdb4382'
    imgfile = 'C:/Users/zqche/Desktop/test2.jpg'
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
    name = result_['result']['name']['words']
    id = result_['result']['id']['words']
    sex = result_['result']['sex']['words']
    birth_date = result_['result']['birth_date']['words']
    description = result_['description']
    error_code = result_['error_code']
    reg_res = str(name) +' '+ str(id) +' '+ str(sex) +' '+ str(birth_date) +' '+ str(description) +' '+ str(error_code) 
    return reg_res

@app.route("/test",methods=["POST"])
def test():
    imgurl = request.json.get("imgurl")
    mysql.commit("UPDATE user SET img='"+imgurl+"' where uid='"+111+"'")
    print(imgurl)

    return str(imgurl)

# @app.route("/user/register/upload", methods=["POST"])
# def hello_world():
#     name = request.form.get("name")
#     description = request.form.get("description")
#     fileObj = request.files.get("file")
#     print(name)
#     print(description)
#     print(fileObj)
#     return "Hello World"

app.run(host="127.0.0.1",port=4444,debug=True) 