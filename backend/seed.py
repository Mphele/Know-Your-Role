import random
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app import models

def seed_database():
    
    models.Base.metadata.drop_all(bind=engine)
    models.Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    tech_stacks = {
        "Backend Developer": ["Python", "SQL", "FastAPI", "Django", "PostgreSQL", "Docker", "AWS", "Go", "Rust"],
        "Frontend Developer": ["JavaScript", "React", "TypeScript", "CSS", "HTML", "Tailwind", "Redux", "Figma"],
        "Full Stack Engineer": ["Python", "JavaScript", "React", "Node.js", "SQL", "AWS", "Docker"],
        "Data Scientist": ["Python", "SQL", "Pandas", "NumPy", "Machine Learning", "TensorFlow", "Statistics"],
        "DevOps Engineer": ["AWS", "Docker", "Kubernetes", "Linux", "Terraform", "CI/CD", "Python", "Bash"]
    }

    seniority_levels = ["Junior", "Mid-Level", "Senior", "Lead", "Intern"]
    
    existing_skills = {}

    print("Seeding Database...")

    for _ in range(50):
        role_title = random.choice(list(tech_stacks.keys()))
        seniority = random.choice(seniority_levels)

        job = models.JobRole(title=role_title, seniority=seniority)
        db.add(job)
        db.commit()
        db.refresh(job)

        potential_skills = tech_stacks[role_title]
        selected_skills_names = random.sample(potential_skills, k=random.randint(3, 5))

        for skill_name in selected_skills_names:
            if skill_name not in existing_skills:
                db_skill = db.query(models.Skill).filter(models.Skill.name == skill_name).first()
                if not db_skill:
                    db_skill = models.Skill(name=skill_name, category="Tech")
                    db.add(db_skill)
                    db.commit()
                    db.refresh(db_skill)
                existing_skills[skill_name] = db_skill
            
            skill_obj = existing_skills[skill_name]
            job.skills.append(skill_obj)
        
        db.commit()
        print(f"Created: {seniority} {role_title}")

    print("Done!")
    db.close()

if __name__ == "__main__":
    seed_database()