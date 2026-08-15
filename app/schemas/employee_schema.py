from pydantic import BaseModel, EmailStr
from decimal import Decimal


class EmployeeCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str | None = None
    department: str | None = None
    designation: str | None = None
    salary: Decimal | None = None


class EmployeeResponse(BaseModel):
    employee_id: int
    first_name: str
    last_name: str
    email: EmailStr
    phone: str | None = None
    department: str | None = None
    designation: str | None = None
    salary: Decimal | None = None

    class Config:
        from_attributes = True

class EmployeeUpdate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str | None = None
    department: str | None = None
    designation: str | None = None
    salary: Decimal | None = None