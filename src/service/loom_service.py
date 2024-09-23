import datetime
from fastapi import HTTPException
from pydantic import *
from fastapi.encoders import jsonable_encoder
from schema.loom_schema import *
from constants.error_const import errormessages
from models import models



class LoomService():
  def __init__(self,app,db):
    self.db = db

  def insertLoom(self,userId,body:InsertLoom):

    # method to maintain number of loom and type of production with the tie-up company
    print("Enter Insert Loom Service")

    new_loom = models.Loom(loomNo=body.loomNo,loomType=body.loomType,tieUp=body.tieUp,productionType=body.productionType)
    self.db.add(new_loom)
    self.db.commit()
    self.db.refresh(new_loom)

    if new_loom == None:
      raise HTTPException(status_code=400, detail=errormessages["1001"])
    
    print("Exit Insert Loom Service")
    return new_loom
  
 

  