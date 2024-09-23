from pymongo import MongoClient
from utils.database import SessionLocal



def connectDb():
  dbclient = MongoClient(host="localhost",port=27017)
  return dbclient

def get_db():
  db = SessionLocal()
  try:
    print(db)
    yield db
  finally:
    db.close()


def close_db_conn(dbclient):
  print("close--2")
  dbclient.close()