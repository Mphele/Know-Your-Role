from pydantic import BaseModel

class JobRoleCreate(BaseModel):
    title:str
    seniority:str = "Mid"

class JobRole(JobRoleCreate):
    id:int
    class Config:
        from_attributes = True

