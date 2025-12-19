from sqlalchemy import Column, Integer, String
from app.database import Base

class JobRole(Base):
    __tablename__ = "job_roles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    seniority = Column(String, default="Mid")

class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index = True)
    name = Column(String, unique=True, index=True)
    category = Column(String)