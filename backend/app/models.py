from sqlalchemy import Column, Integer, String, Date, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)       # auto-increment ID
    employee_id = Column(String(50), unique=True, nullable=False, index=True)  # unique employee ID
    full_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False, index=True)
    department = Column(String(50), nullable=False)

class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"), nullable=False)
    date = Column(Date, nullable=False)
    status = Column(String(10), nullable=False)  # Present / Absent

    employee = relationship("Employee", backref="attendance_records")