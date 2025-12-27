from fastapi import FastAPI , Depends, HTTPException
from . import models, schemas, crud
from .database import engine, get_db
from sqlalchemy.orm import Session
from typing import List, Optional


models.Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.post("/roles/", response_model=schemas.JobRole)
def create_role(role:schemas.JobRoleCreate, db:Session=Depends(get_db)):
    return crud.create_job_role(db,role)

@app.get("/roles/", response_model=List[schemas.JobRole])
def read_roles(skip: int = 0, limit: int = 100, seniority:Optional[str]=None, db: Session = Depends(get_db)):
    roles = crud.get_job_roles(db, skip=skip, limit=limit, seniority=seniority)
    return roles

@app.post("/skills/", response_model=schemas.Skill)
def create_skill(skill:schemas.SkillCreate, db:Session=Depends(get_db)):
    return crud.create_job_skill(db,skill)

@app.get("/skills/", response_model=List[schemas.Skill])
def read_skills(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    skills = crud.get_job_skills(db,skip,limit)
    return skills

@app.post("/roles/{role_id}/skills/{skill_id}")
def connect_skill_to_role(role_id:int, skill_id:int, db:Session=Depends(get_db)):
    role = crud.add_skill_to_role(db, role_id, skill_id)
    if role is None:
        raise HTTPException(status_code=404, detail="Role or Skill not found")
    return role

@app.delete("/roles/{role_id}",status_code=204)
def delete_role(role_id:int, db: Session = Depends(get_db)):
    role = crud.delete_job_role(db,role_id)
    if role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return None

@app.put("/roles/{role_id}", response_model=schemas.JobRole)
def update_role(role_id:int, new_role:schemas.JobRoleCreate, db:Session=Depends(get_db)):
    role = crud.edit_job_role(db,role_id,new_role)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    
    return role

@app.delete('/skills/{skill_id}', status_code=204)
def delete_skill(skill_id:int, db:Session = Depends(get_db)):
    skill = crud.delete_job_skill(db=db,skill_id=skill_id)
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    
    return None

@app.put("/skills/{skill_id}",response_model=schemas.Skill)
def update_skill(skill_id:int,new_skill:schemas.SkillCreate,db:Session = Depends(get_db)):
    skill = crud.edit_job_skill(db=db, new_skill=new_skill, skill_id=skill_id)
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    
    return skill