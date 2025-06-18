from pymongo import MongoClient
mongo=MongoClient("localhost:27017")
db=mongo.college
students=db.students