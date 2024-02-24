from fastapi import APIRouter, Request, Response


router = APIRouter()

@router.post("/insert")
def insertProduction():
  print("production  insert")
  
