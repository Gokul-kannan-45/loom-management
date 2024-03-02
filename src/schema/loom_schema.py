from pydantic import BaseModel

class InsertLoom(BaseModel):
  loomNo : int = None
  loomType : str = None
  tieUp : str= None
  productionType : str = None