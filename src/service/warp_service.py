import datetime

class WarpService():
  def __init__(self,app,userId=None):
    self.warpDb = app.database['warp'] 
    pass

  def getWarp(self,userId):
    print("**************")
    print(self.warpDb)
    warpObj = self.warpDb.find_one({"id":1001},{"_id":0})
    print(warpObj)
    print("inside getWarp method")
    return warpObj