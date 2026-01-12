from sqlalchemy import Column, Integer, String, Table, ForeignKey
from app.database import Base
from sqlalchemy.orm import relationship

role_skills = Table(
    "role_skills",
    Base.metadata,
    Column("job_role_id", Integer, ForeignKey("job_roles.id"), primary_key=True),
    Column("skill_id", Integer, ForeignKey("skills.id"), primary_key=True)
)

class JobRole(Base):
    __tablename__ = "job_roles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=False, index=True)
    seniority = Column(String, default="Mid")
    skills = relationship("Skill", secondary=role_skills, back_populates="job_roles")

class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index = True)
    name = Column(String, unique=True, index=True)
    category = Column(String)
    job_roles = relationship("JobRole", secondary=role_skills, back_populates="skills")

