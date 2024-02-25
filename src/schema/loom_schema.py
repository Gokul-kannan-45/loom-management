from pydantic import BaseModel

class Item(BaseModel):
  loomNo : int = None
  loomType : str = None
  tieUp : str= None
  productionType : str = None