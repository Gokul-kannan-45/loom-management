from fastapi import APIRouter, Request, Response, Header, status
from service.loom_service import LoomService
from schema.loom_schema import Item
from schema.response_schema import ApiResponse

router = APIRouter()

@router.post("/loom/insert",response_model=ApiResponse,status_code=status.HTTP_200_OK)
def insertLoom(request:Request, response:Response, userId:str = Header(..., alias='userId'), body:Item =...):
  
  service = LoomService(request.app)
  insrtloom = service.insertLoom(userId,body)
  print(insrtloom)
  resp = ApiResponse(code=status.HTTP_200_OK,status="SUCCESS",data={"status":"Loom Record Inserted.."})
  return resp


