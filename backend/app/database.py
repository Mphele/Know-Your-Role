from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. Connection String
# Format: postgresql://<username>:<password>@<host>:<port>/<database_name>
# REPLACE 'YOUR_PASSWORD' with your actual password.
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Moswane1@localhost:1739/knowyourrole"

# 2. The Engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# 3. The Session Factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. The Base Class
Base = declarative_base()

# 5. Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Temporary Test Block ---
if __name__ == "__main__":
    try:
        # Try to connect
        with engine.connect() as connection:
            print("Successfully connected to the PostgreSQL database on port 1739!")
    except Exception as e:
        print(f"Connection failed: {e}")