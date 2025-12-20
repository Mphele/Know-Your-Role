import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

password = os.getenv("DATABASE_PASSWORD")

SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:{password}@localhost:1739/knowyourrole"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

if __name__ == "__main__":
    try:
        with engine.connect() as connection:
            print("Successfully connected to the PostgreSQL database on port 1739!")
    except Exception as e:
        print(f"Connection failed: {e}")