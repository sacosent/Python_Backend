from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

class User(BaseModel):
    username: str
    email: str
    disabled: bool

class UserDB(User):
    password: str


users_db = {
    "sacosent": {
        "username": "sacosent",
        "email": "cosentinosantiago92@gmail.com",
        "disabled": False,
        "password": "Prueba123",
    },
    "cogesto": {
        "username": "cogesto",
        "email": "constanzagestoso@gmail.com",
        "disabled": True,
        "password": "Prueba456"
    }
}

def search_user_db(username: str):
    return UserDB(**users_db[username])


def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])
    
async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token",
            headers={"WWW-Authenticate": "Bearer"})

    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User disabled")

    return user


@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail="User not found")
    
    user = search_user_db(form.username)

    if not form.password == user.password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail="Invalid Password")
    
    return {"access_tokern": user.username, "token_type": "bearer"}

@app.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user