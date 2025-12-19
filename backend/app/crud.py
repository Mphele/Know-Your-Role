from sqlalchemy.orm import Session
from . import models, schemas

def create_job_role(db:Session, role:schemas.JobRoleCreate):
    model = models.JobRole(title=role.title, seniority = role.seniority)
    db.add(model)
    db.commit()
    db.refresh(model)

    return model

def get_job_roles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.JobRole).offset(skip).limit(limit).all()

def create_job_skill(db:Session, skill:schemas.SkillCreate):
    model = models.Skill(name=skill.name, category = skill.category)
    db.add(model)
    db.commit()
    db.refresh(model)

    return model

def get_job_skills(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Skill).offset(skip).limit(limit).all()
