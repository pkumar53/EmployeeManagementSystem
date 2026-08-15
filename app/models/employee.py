from sqlalchemy import Column, Integer, String, DECIMAL

from app.database import Base


class Employee(Base):

    __tablename__ = "employee"

    employee_id = Column(Integer, primary_key=True, autoincrement=True)

    first_name = Column(String(100), nullable=False)

    last_name = Column(String(100), nullable=False)

    email = Column(String(150), nullable=False, unique=True)

    phone = Column(String(20))

    department = Column(String(100))

    designation = Column(String(100))

    salary = Column(DECIMAL(12, 2))