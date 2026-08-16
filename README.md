# Employee Management System - Backend

Backend REST API for the Employee Management System built using **Python, FastAPI, SQLAlchemy, and MySQL**.

The application provides APIs to:

- View all employees
- View an employee by ID
- Add a new employee
- Update an existing employee
- Delete an employee

## Technology Stack

- Python 3.13+
- FastAPI
- Uvicorn
- SQLAlchemy
- PyMySQL
- Pydantic
- MySQL
- python-dotenv

## Project Structure

```text
EmployeeManagementSystem/
│
├── app/
│   ├── controllers/
│   │   └── employee_controller.py
│   │
│   ├── models/
│   │   └── employee.py
│   │
│   ├── repositories/
│   │   └── employee_repository.py
│   │
│   ├── schemas/
│   │   └── employee_schema.py
│   │
│   ├── services/
│   │   └── employee_service.py
│   │
│   ├── database.py
│   └── main.py
│
├── database/
│   └── schema.sql
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## To Execute
git clone https://github.com/pkumar53/EmployeeManagementSystem.git
cd EmployeeManagementSystem
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
http://localhost:8000/docs
