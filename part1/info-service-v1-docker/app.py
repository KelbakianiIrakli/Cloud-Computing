
from flask import Flask
from flask import jsonify
import os
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.sql import select
from flask import request
import config
from flask_swagger_ui import get_swaggerui_blueprint

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
    return "APi working"

@app.rout('/static/<path:path>')
def send_static(path):
    return send_from_dictionary('static', path)
    ### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Seans-Python-Flask-REST-Boilerplate"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###
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
    with engine.connect() as conn:
        result = conn.execute(text("INSERT INTO watches(sku, type, gender, year, dial_material, case_material, bracelet_material, movement) VALUES('"+sku+"','"+watch_type+"','"+gender+"', '"+str(year)+"', '"+dial_material+"', '"+case_material+"', '"+bracelet_material+"', '"+movement+"')"))
        return str(result)

# INSERT INTO watches(sku, type, gender, year, dial_material, case_material, bracelet_material, movement)
# VALUES('"+sku+"','"+watch_type+"','"+gender+"', '"+year+"', '"+dial_material+"', '"+case_material+"', '"+bracelet_material+"', '"+movement+"');

@app.route("/watch/search/<sku>",methods=["GET"])
def getSearchedWatch(sku=None):
    print("search get")
    with engine.connect() as conn:
        result = conn.execute(text("select * from watches where watches.sku like '"+sku+"'")).fetchall()
        return str(result)
            
@app.route("/watch/<sku>",methods=["GET"])
def getWatch(sku=None):
    print("normal get")
    with engine.connect() as conn:
        result = conn.execute(text("select * from watches where watches.sku = '"+sku+"'")).fetchone()
        print(result)
        return str(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT, debug=config.DEBUG_MODE)

