import uvicorn
from fastapi import FastAPI

from app.routers import mkroutes
from utils.mktik import get_mk_address_list
import config


app = FastAPI()


@app.on_event("startup")
async def startup():
    #    await database.connect()
    print("server start, mktik ip is: ", config.MKTIK_IP)


@app.on_event("shutdown")
async def shutdown():
    #    await database.disconnect()
    print("server stop")


app.include_router(mkroutes.router)

if __name__ == '__main__':
#    get_mk_address_list()
    uvicorn.run(app, host="127.0.0.1", port=8000)
