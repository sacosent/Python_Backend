from fastapi import FastAPI
from routers import products, users, jwt_auth
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Routers
app.include_router(products.router)
app.include_router(users.router)
app.include_router(jwt_auth.router)
app.mount("/static",StaticFiles(directory="static"),name="static")


@app.get("/")
async def root():
    return {"Hello": "World"}


