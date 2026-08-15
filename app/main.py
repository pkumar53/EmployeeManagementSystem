from fastapi import FastAPI

from app.controllers.employee_controller import router as employee_router

app = FastAPI(
    title="Employee Management System"
)

app.include_router(employee_router)


@app.get("/")
def home():
    return {
        "message": "Employee Management System API is running"
    }