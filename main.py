from fastapi import FastAPI
import uvicorn
from db.base import database
from endpoints import users, auth

app = FastAPI(title="Employement exchange")
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


if __name__ == "__main__":
    uvicorn.run("main:app", port=5432, host="127.0.0.1", reload=True)