from fastapi import APIRouter


auth_router = APIRouter(
    prefix="/auth",
    tags=["user_auth"]
)


@auth_router.post("/register")
def register_user():
    return {"message": "User registered!"}


@auth_router.post("/login")
def login():
    return {"message": "User logged in!"}