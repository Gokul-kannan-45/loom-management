from fastapi import APIRouter, Request, Response


router = APIRouter()

@router.post("/production/insert")
def insertProduction():
  print("production  insert")
  
