from sqlalchemy.orm import Session
from . import models, schemas

# Create new employee
def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = models.Employee(
        employee_id=employee.employee_id,
        full_name=employee.full_name,
        email=employee.email,
        department=employee.department
    )
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

# Get all employees
def get_employees(db: Session):
    return db.query(models.Employee).all()

# Get employee by ID
def get_employee(db: Session, employee_id: int):
    return db.query(models.Employee).filter(models.Employee.id == employee_id).first()

# Delete employee
def delete_employee(db: Session, employee_id: int):
    employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if employee:
        db.delete(employee)
        db.commit()
    return employee

def create_attendance(db: Session, attendance: schemas.AttendanceCreate):
    db_attendance = models.Attendance(
        employee_id=attendance.employee_id,
        date=attendance.date,
        status=attendance.status
    )
    db.add(db_attendance)
    db.commit()
    db.refresh(db_attendance)
    return db_attendance

def get_attendance_by_employee(db: Session, employee_id: int):
    return db.query(models.Attendance).filter(models.Attendance.employee_id == employee_id).all()

