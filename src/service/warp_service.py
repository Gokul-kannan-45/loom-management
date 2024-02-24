import datetime

class WarpService():
  def __init__(self,app,userId=None):
    self.warpDb = app.database['loom'] 
    pass

  def getWarp(self,userId):
    print("**************")
    print(self.warpDb)
    warpObj = self.warpDb.find({"name":"Gokul"},{"_id":0})
    print(warpObj)
    print("inside getWarp method")
    return warpObj