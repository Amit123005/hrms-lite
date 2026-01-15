from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, database

router = APIRouter(
    prefix="/attendance",
    tags=["Attendance"]
)

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.AttendanceResponse)
def mark_attendance(attendance: schemas.AttendanceCreate, db: Session = Depends(get_db)):
    from .. import models
    if not db.query(models.Employee).filter(models.Employee.id == attendance.employee_id).first():
        raise HTTPException(status_code=404, detail="Employee not found")
    return crud.create_attendance(db, attendance)

@router.get("/{employee_id}", response_model=list[schemas.AttendanceResponse])
def get_attendance(employee_id: int, db: Session = Depends(get_db)):
    records = crud.get_attendance_by_employee(db, employee_id)
    if not records:
        raise HTTPException(status_code=404, detail="No attendance found for this employee")
    return records