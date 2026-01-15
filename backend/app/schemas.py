from pydantic import BaseModel, EmailStr
from datetime import date

# For creating employee
class EmployeeCreate(BaseModel):
    employee_id: str
    full_name: str
    email: EmailStr
    department: str

# For returning employee info
class EmployeeResponse(BaseModel):
    id: int
    employee_id: str
    full_name: str
    email: EmailStr
    department: str

    class Config:
        orm_mode = True

class AttendanceCreate(BaseModel):
    employee_id: int
    date: date
    status: str  # "Present" or "Absent"

class AttendanceResponse(BaseModel):
    id: int
    employee_id: int
    date: date
    status: str

    class Config:
        orm_mode = True
