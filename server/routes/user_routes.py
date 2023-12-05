from fastapi import APIRouter


user_router = APIRouter(
    prefix="/user",
    tags=["user_profile"]
)


@user_router.get("/")
def get_users():
    return {"message", "All users"}


@user_router.get("/:id")
def get_user_by_id(id):
    return {"message": f"User ID: {id}"}