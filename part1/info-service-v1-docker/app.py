
from flask import Flask
from flask import jsonify

from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.sql import select
class Watch:
    def __init__(self, row):
        self.sku = row[0]
        self.type = row[1]
        self.gender = row[2]
        self.year = row[3]
        self.dial_material = row[4]
        self.case_material = row[5]
        self.bracelet_material = row[6]
        self.movement = row[7]

engine = create_engine("mysql+pymysql://root:root@localhost/cloud_computing")

app = Flask(__name__)


@app.route("/watch/",methods=["POST"])
def addWatch():
    print("watfjedjsfjksdjfsch")
    return "<p>Hello, World!</p>",200

@app.route("/watch/search<sku>",methods=["GET"])
def getSearchedWatch(sku=None):
    print("search get")
    with engine.connect() as conn:
        result = conn.execute(text("select * from watches where watches.sku like '"+sku+"'"))
        try:
            tr = (Watch(r) for r in result)
            return jsonify((dict((key, value) for key, value in tmpWatch.__dict__.items() if not callable(value) and not key.startswith('__')for tmpWatch in tr)))
        except:
            return 404
            
@app.route("/watch/<sku>",methods=["GET"])
def getWatch(sku=None):
    print("normal get")
    with engine.connect() as conn:
        result = conn.execute(text("select * from watches where watches.sku = '"+sku+"'"))
    for r in result:
        watch = Watch(r);
    return jsonify(dict((key, value) for key, value in watch.__dict__.items() if not callable(value) and not key.startswith('__')))
