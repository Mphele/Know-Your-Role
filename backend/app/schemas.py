from pydantic import BaseModel
from typing import List


class SkillCreate(BaseModel):
    name:str
    category:str=None

class Skill(SkillCreate):
    id:int
    class Config:
        from_attributes=True

class JobRoleCreate(BaseModel):
    title:str
    seniority:str = "Mid"

class JobRole(JobRoleCreate):
    id:int
    class Config:
        from_attributes = True
    skills:List[Skill]=[]
    

