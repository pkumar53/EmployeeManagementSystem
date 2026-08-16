from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.controllers.employee_controller import router as employee_router

app = FastAPI(
    title="Employee Management System"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173","https://employeemanagementsystemui.onrender.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(employee_router)


@app.get("/")
def home():
    return {
        "message": "Employee Management System API is running"
    }