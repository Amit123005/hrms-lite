from fastapi import FastAPI
from .routers import employee
from .database import Base, engine

app = FastAPI(title="HRMS Lite API", version="1.0.0")

# Create tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(employee.router)

@app.get("/")
def health_check():
    return {"status": "HRMS Lite backend running"}
