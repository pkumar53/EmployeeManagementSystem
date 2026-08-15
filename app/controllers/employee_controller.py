from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.services.employee_service import EmployeeService
from app.models.employee import Employee
from fastapi import HTTPException
from app.schemas.employee_schema import (
    EmployeeCreate,
    EmployeeResponse,
    EmployeeUpdate
)
router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)

employee_service = EmployeeService()


@router.get("/", response_model=list[EmployeeResponse])
def get_employees(db: Session = Depends(get_db)):
    return employee_service.get_all_employees(db)

@router.get("/{employee_id}", response_model=EmployeeResponse)
def get_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):
    employee = employee_service.get_employee(db, employee_id)

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee

@router.post("/", response_model=EmployeeResponse)
def create_employee(
    employee_data: EmployeeCreate,
    db: Session = Depends(get_db)
):
    employee = Employee(
        first_name=employee_data.first_name,
        last_name=employee_data.last_name,
        email=employee_data.email,
        phone=employee_data.phone,
        department=employee_data.department,
        designation=employee_data.designation,
        salary=employee_data.salary
    )

    return employee_service.create_employee(db, employee)

@router.put("/{employee_id}", response_model=EmployeeResponse)
def update_employee(
    employee_id: int,
    employee_data: EmployeeUpdate,
    db: Session = Depends(get_db)
):
    employee = employee_service.update_employee(
        db,
        employee_id,
        employee_data
    )

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee

@router.delete("/{employee_id}")
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):
    deleted = employee_service.delete_employee(
        db,
        employee_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return {
        "message": "Employee deleted successfully"
    }