from sqlalchemy.orm import Session

from app.models.employee import Employee


class EmployeeRepository:

    def find_all(self, db: Session):
        return db.query(Employee).all()

    def find_by_id(self, db: Session, employee_id: int):
        return db.query(Employee).filter(
            Employee.employee_id == employee_id
        ).first()

    def save(self, db: Session, employee: Employee):
        db.add(employee)
        db.commit()
        db.refresh(employee)

        return employee

    def delete(self, db: Session, employee: Employee):
        db.delete(employee)
        db.commit()

    def update(self, db: Session, employee: Employee):
        db.commit()
        db.refresh(employee)
        return employee