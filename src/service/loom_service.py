import datetime
from fastapi import HTTPException
from pydantic import *
from fastapi.encoders import jsonable_encoder
from schema.loom_schema import *
from constants.error_const import errormessages


class LoomService():
  def __init__(self,app):
    self.loomDb = app.database['loom']

  def insertLoom(self,userId,body:InsertLoom):

    # method to maintain number of loom and type of production with the tie-up company
    print("Enter Insert Loom Service")
    body = jsonable_encoder(body)
    filter = {"loomNo":body["loomNo"]}
    loomObj = self.loomDb.find_one(filter,{"_id":0})
    print(loomObj)

    if loomObj != None:
      raise HTTPException(status_code=400, detail=errormessages["1001"])
    
    recordInsert = self.loomDb.insert_one(body).inserted_id
    print("Exit Insert Loom Service")
    return recordInsert
  
  def updateLoom(self, userId, body):
    print("Enter update loom method")

  