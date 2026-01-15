from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, crud, database

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create employee
@router.post("/", response_model=schemas.EmployeeResponse)
def create_employee_endpoint(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    # Check for duplicate employee_id or email
    if db.query(models.Employee).filter(
        (models.Employee.employee_id == employee.employee_id) |
        (models.Employee.email == employee.email)
    ).first():
        raise HTTPException(status_code=400, detail="Employee ID or Email already exists")
    return crud.create_employee(db, employee)

# Get all employees
@router.get("/", response_model=list[schemas.EmployeeResponse])
def get_employees_endpoint(db: Session = Depends(get_db)):
    return crud.get_employees(db)

# Delete employee
@router.delete("/{employee_id}", response_model=schemas.EmployeeResponse)
def delete_employee_endpoint(employee_id: int, db: Session = Depends(get_db)):
    employee = crud.delete_employee(db, employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee
