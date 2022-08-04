import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from app.routers import mkroutes
from app.config import MKTIK_IP


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

origins = [
    "*",
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    #    await database.connect()
    print("server start, mktik ip is: ", MKTIK_IP)


@app.on_event("shutdown")
async def shutdown():
    #    await database.disconnect()
    print("server stop")


app.include_router(mkroutes.router)

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)


"""
    для русских букв надо в  routeros_api/api_strycture.py заменить на:
    def get_python_value(self, bytes):
        return bytes.decode('cp1251', "ignore")
"""