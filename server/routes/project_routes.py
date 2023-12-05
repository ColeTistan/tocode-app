from fastapi import APIRouter


project_router = APIRouter(
    prefix="/project",
    tags=["project"]
)


@project_router.get("/")
def get_projects():
    return {"message", "All projects"}


@project_router.get("/:id")
def get_project_by_id(id):
    return {"message": f"Project ID: {id}"}