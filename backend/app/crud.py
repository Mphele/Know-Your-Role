from sqlalchemy.orm import Session
from . import models, schemas

def create_job_role(db:Session, role:schemas.JobRoleCreate):
    model = models.JobRole(title=role.title, seniority = role.seniority)
    db.add(model)
    db.commit()
    db.refresh(model)

    return model

def get_job_roles(db: Session, skip: int = 0, limit: int = 100,seniority:str=''):
    query = db.query(models.JobRole)
    if seniority:
            return query.filter(models.JobRole.seniority==seniority).offset(skip).limit(limit).all()

    return query.offset(skip).limit(limit).all()

def create_job_skill(db:Session, skill:schemas.SkillCreate):
    model = models.Skill(name=skill.name, category = skill.category)
    db.add(model)
    db.commit()
    db.refresh(model)

    return model

def get_job_skills(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Skill).offset(skip).limit(limit).all()


def add_skill_to_role(db:Session, role_id:int, skill_id:int):
    role = db.query(models.JobRole).filter(models.JobRole.id == role_id).first()
    
    skill = db.query(models.Skill).filter(models.Skill.id == skill_id).first()

    if not role or not skill:
        return None

    role.skills.append(skill)
    db.commit()
    db.refresh(role)
    return role


def delete_job_role(db:Session, role_id:int):
    role = db.query(models.JobRole).filter(models.JobRole.id == role_id).first()

    if not role:
        return None
    
    db.delete(role)
    db.commit()

    return role


def edit_job_role(db:Session, role_id:int, new_role:schemas.JobRoleCreate):
   role= db.query(models.JobRole).filter(models.JobRole.id==role_id).first()
   if not role:
       return None
   role.title=new_role.title
   role.seniority = new_role.seniority
   db.commit()
   db.refresh(role)
   return role

def edit_job_skill(db:Session, skill_id:int, new_skill:schemas.SkillCreate):
    skill = db.query(models.Skill).filter(models.Skill.id==skill_id).first()
    if not skill:
        return None
    skill.name = new_skill.name
    skill.category=new_skill.category

    db.commit()
    db.refresh(skill)
    
    return skill

def delete_job_skill(db:Session, skill_id:int):
    skill = db.query(models.Skill).filter(models.Skill.id==skill_id).first()
    if not skill:
        return None
    
    db.delete(skill)
    db.commit()
    
    return skill