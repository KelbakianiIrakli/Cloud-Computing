
from flask import Flask
from flask import jsonify
import os
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.sql import select
from flask import request
import config
# class Watch:
#     def __init__(self, row):
#         self.sku = row[0]
#         self.type = row[1]
#         self.gender = row[2]
#         self.year = row[3]
#         self.dial_material = row[4]
#         self.case_material = row[5]
#         self.bracelet_material = row[6]
#         self.movement = row[7]

# engine = create_engine("mysql+pymysql://root:root@localhost/cloud_computing")
engine = create_engine("mysql+pymysql://root:root1234@10.92.32.3/watch")


app = Flask(__name__)

@app.route("/",methods=["GET"])
def healthCheck(sku=None):
    return "API is working working"

@app.route("/watch/",methods=["POST"])
def addWatch():
    print("add watch")
    request_data = request.get_json()
    print(request_data)
    sku = request_data["sku"]
    watch_type = request_data["type"]
    gender = request_data["gender"]
    year = request_data["year"]
    print(type(year))
    dial_material = request_data["dial_material"]
    case_material = request_data["case_material"]
    bracelet_material = request_data["bracelet_material"]
    movement = request_data["movement"]
    try:
        with engine.connect() as conn:
            result = conn.execute(text("INSERT INTO watches(sku, type, gender, year, dial_material, case_material, bracelet_material, movement) VALUES('"+sku+"','"+watch_type+"','"+gender+"', '"+str(year)+"', '"+dial_material+"', '"+case_material+"', '"+bracelet_material+"', '"+movement+"')"))
            return str(result)
    except:
        print("Something went wrong ")
        return "Something went wrong"

# INSERT INTO watches(sku, type, gender, year, dial_material, case_material, bracelet_material, movement)
# VALUES('"+sku+"','"+watch_type+"','"+gender+"', '"+year+"', '"+dial_material+"', '"+case_material+"', '"+bracelet_material+"', '"+movement+"');

@app.route("/watch/search/<sku>",methods=["GET"])
def getSearchedWatch(sku=None):
    print("search get")
    try:
        with engine.connect() as conn:
            result = conn.execute(text("select * from watches where watches.sku like '"+sku+"'")).fetchall()
            return str(result)
    except:
        print("Something went wrong ")
        return "Something went wrong"


@app.route("/watch/<sku>",methods=["GET"])
def getWatch(sku=None):
    print("normal get")
    try:
        with engine.connect() as conn:
            result = conn.execute(text("select * from watches where watches.sku = '"+sku+"'")).fetchone()
            print(result)
            return str(result)
    except:
        print("Something went wrong ")
        return "Something went wrong"


@app.route("/watch/delete/<sku>",methods=["POST"])
def getWatch(sku=None):
    try:
        with engine.connect() as conn:
            result = conn.execute(text("select * from watches where watches.sku = '"+sku+"'")).fetchone()
            if len(result) == 1:
                esult = conn.execute(text("delete * from watches where watches.sku = '"+sku+"'")).fetchone()
                print(result)
                return str(result)

    except:
        print("Something went wrong ")
        return "Something went wrong"




"""
no sql calls
"""


import pymongo
from pymongo import MongoClient
# client = MongoClient('localhost', 27017)
# db = client['project2']


client = pymongo.MongoClient("mongodb+srv://root:root1234@cluster0.gyuxkjj.mongodb.net/?w=majority")
db = client.watches
collection = db['watches']

@app.route("/watch_mongo/",methods=["POST"])
def addWatch_mongo():
    print("add watch")
    request_data = request.get_json()
    print(request_data)
    sku = request_data["sku"]
    watch_type = request_data["type"]
    gender = request_data["gender"]
    year = request_data["year"]
    print(type(year))
    dial_material = request_data["dial_material"]
    case_material = request_data["case_material"]
    bracelet_material = request_data["bracelet_material"]
    movement = request_data["movement"]
    try:
        collection.insert({"sku":sku, "type":watch_type, "gender":gender, "year":year, "dial_material":dial_material,"case_material":case_material,"bracelet_material":bracelet_material,"movement":movement})
        return "Done"
    except:
        print("Something went wrong ")
        return "Something went wrong"


@app.route("/watch/search_mongo/<sku>",methods=["GET"])
def getSearchedWatch_mongo(sku=None):
    print("search get", sku)
    res = []
    try:
        for x in collection.find({"sku":{"$regex":sku}}):
            res.append(x)
            print(x)
        return str(res)
    except:
        print("Something went wrong ")
        return "Something went wrong"
    
            
@app.route("/watch_mongo/<sku>",methods=["GET"])
def getWatch_mongo(sku=None):
    print("normal get", sku)
    try:
        x = collection.find_one({"sku":sku})
        return str(x)
    except:
        print("Something went wrong ")
        return "Something went wrong"

@app.route("/watch_mongo/delete/<sku>",methods=["POST"])
def getWatch_mongo(sku=None):
    print("normal get", sku)
    try:
        x = collection.find_one({"sku":sku})
        if len(x) == 1:
            collection.delete({"sku":sku})
            return "Done"
    except:
        print("Something went wrong ")
        return "Something went wrong"

    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT, debug=config.DEBUG_MODE)

