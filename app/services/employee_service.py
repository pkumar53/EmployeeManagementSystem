from sqlalchemy.orm import Session

from app.models.employee import Employee
from app.repositories.employee_repository import EmployeeRepository


class EmployeeService:

    def __init__(self):
        self.repository = EmployeeRepository()

    def get_all_employees(self, db: Session):
        return self.repository.find_all(db)

    def get_employee(self, db: Session, employee_id: int):
        return self.repository.find_by_id(db, employee_id)

    def create_employee(self, db: Session, employee: Employee):
        return self.repository.save(db, employee)

    def delete_employee(self, db: Session, employee_id: int):
        employee = self.repository.find_by_id(db, employee_id)

        if employee is None:
            return False

        self.repository.delete(db, employee)

        return True

    def update_employee(
        self,
        db: Session,
        employee_id: int,
        employee_data
    ):
        employee = self.repository.find_by_id(db, employee_id)

        if employee is None:
            return None

        employee.first_name = employee_data.first_name
        employee.last_name = employee_data.last_name
        employee.email = employee_data.email
        employee.phone = employee_data.phone
        employee.department = employee_data.department
        employee.designation = employee_data.designation
        employee.salary = employee_data.salary

        return self.repository.update(db, employee)