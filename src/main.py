from fastapi import FastAPI
import uvicorn
#from loom-src.routing import warp_router, production_router
from routing import warp_router,production_router
from utils.dbutils import connectDb, get_db

app = FastAPI(openapi_url="/app/loom/manage/openapi.json",docs_url="/app/loom/manage/docs")

@app.on_event("startup")
def startup_db_client():
  app.mongo_client = connectDb()
  app.database = get_db(app.mongo_client)
  print("DB Connected")

@app.on_event("shutdown")
def shutdown_db_client():
  print("close")
  app.mongo_client.close()


app.include_router(warp_router.router, prefix="/app/loom/warp", tags=["Warp Management"])
app.include_router(production_router.router, prefix="/app/loom/production", tags=["Production Management"])

if __name__ == '__main__':
  uvicorn.run(app, host='127.0.0.1', port=4200)
