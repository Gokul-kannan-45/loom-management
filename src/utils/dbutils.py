from pymongo import MongoClient



def connectDb():
  dbclient = MongoClient(host="localhost",port=27017)
  return dbclient

def get_db(dbclient)->MongoClient:
  return dbclient["mydatabase"]

def close_db_conn(dbclient):
  print("close--2")
  dbclient.close()