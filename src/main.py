from fastapi import FastAPI
import uvicorn
from routing import warp_router,production_router,loom_router
from utils.dbutils import connectDb, get_db
from logger import get_logger

logger = get_logger()

app = FastAPI(openapi_url="/app/loom/manage/openapi.json",docs_url="/app/loom/manage/docs")

@app.on_event("startup")
def startup_db_client():
  app.mongo_client = connectDb()
  app.database = get_db(app.mongo_client)
  logger.info("DB connected")

@app.on_event("shutdown")
def shutdown_db_client():
  logger.info("DB Disconnected")
  app.mongo_client.close()

app.include_router(loom_router.router, prefix="/app", tags=["Loom Management"])
app.include_router(warp_router.router, prefix="/app", tags=["Warp Management"])
app.include_router(production_router.router, prefix="/app", tags=["Production Management"])

if __name__ == '__main__':
  uvicorn.run(app, host='0.0.0.0', port=4200)
