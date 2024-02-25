from schema.loom_schema import Item
from fastapi.encoders import jsonable_encoder

class LoomService():
  def __init__(self,app):
    self.loomDb = app.database['loom']

  def insertLoom(self,userId,body):
    print("inside Insert Loom Service")
    body = jsonable_encoder(body)
    recordInsert = self.loomDb.insert_one(body).inserted_id
    return recordInsert

  