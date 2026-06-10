from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/users")
def create_user(user: User):
    return {"message": "User created", "user": user}
    
@app.get("/users")
def get_users():
    return {"message": "Users retrieved"}