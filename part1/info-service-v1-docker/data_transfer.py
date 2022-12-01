import pymongo
from pymongo import MongoClient
from sqlalchemy import create_engine
from sqlalchemy import text
# client = MongoClient('localhost', 27017)
# db = client['project2']


client = pymongo.MongoClient("mongodb+srv://root:root1234@cluster0.gyuxkjj.mongodb.net/?w=majority")
engine = create_engine("mysql+pymysql://root:root1234@localhost/sys")
db = client.watches
collection = db['watches']

from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.sql import select
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import declarative_base
from flask import request



# watch = Table("watches", metadata_obj, Column("sku", String, primary_key=True), Column("type", String), Column("gender", String),
#  Column("year", String), Column("dial_material", String))


# engine = create_engine("mysql+pymysql://root:root1234@localhost/sys")
engine = create_engine("mysql+pymysql://root:root1234@34.75.212.230/watch")
# metadata_obj.create_all(engine)

sku = "A%"

write_arr = []
with engine.connect() as conn:
	result = conn.execute(text("select * from watches ")).fetchall()
	for request_data in result:
		sku = request_data[0]
		watch_type = request_data[1]
		gender = request_data[2]
		year = request_data[3]
		# print(type(year))
		dial_material = request_data[4]
		case_material = request_data[5]
		bracelet_material = request_data[6]
		movement = request_data[7]
		write_arr.append({"sku":sku, "type":watch_type, "gender":gender, \
	"year":year, "dial_material":dial_material,"case_material":case_material,"bracelet_material":bracelet_material,"movement":movement})
	collection.insert_many(write_arr)
