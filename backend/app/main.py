from fastapi import FastAPI , Depends
from . import models, schemas, crud
from .database import engine, get_db
from sqlalchemy.orm import Session
from typing import List



models.Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.post("/roles/", response_model=schemas.JobRole)
def create_role(role:schemas.JobRoleCreate, db:Session=Depends(get_db)):
    return crud.create_job_role(db,role)

@app.get("/roles/", response_model=List[schemas.JobRole])
def read_roles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    roles = crud.get_job_roles(db, skip=skip, limit=limit)
    return roles

