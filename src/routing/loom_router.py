from fastapi import APIRouter, Request, Response, Header, status, Depends
from service.loom_service import LoomService
from schema.loom_schema import *
from schema.response_schema import ApiResponse
from sqlalchemy.orm import Session
from utils.dbutils import connectDb, get_db


router = APIRouter()

@router.post("/loom/insert",response_model=ApiResponse,status_code=status.HTTP_200_OK)
def insertLoom(request:Request, response:Response, db: Session = Depends(get_db), userId:str = Header(..., alias='userId'), body:InsertLoom =...):
  
  service = LoomService(request.app,db)
  insrtloom = service.insertLoom(userId,body)
  print(insrtloom)
  resp = ApiResponse(code=status.HTTP_200_OK,status="SUCCESS",data={"status":"Loom Record Inserted.."})
  return resp



