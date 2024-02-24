from fastapi import APIRouter, Request, Response
from service.warp_service import WarpService

router = APIRouter()

@router.post("/create")
def createWarp(request:Request,response:Response,userId:str):
  print("production  insert")
  service = WarpService(request.app,userId)
  warp = service.getWarp(userId)
  return warp