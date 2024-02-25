from pydantic import BaseModel,Field
from typing import Optional

class ApiResponse(BaseModel):
  code:int=Field(default=200)
  status:str=Field(default="SUCCESS")
  data:Optional[dict]