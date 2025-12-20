# KnowYourRole – Backend API

The backend service for the **KnowYourRole** application.  
It handles data persistence, business logic, and API endpoints using **FastAPI** and **PostgreSQL**.

---

## Directory Structure

The backend code resides in the `backend/` directory.

```

Know-Your-Role/
├── backend/             <-- You are here
│   ├── .env             <-- Secrets file (Database Password)
│   ├── requirements.txt <-- Python dependencies
│   ├── venv/            <-- Virtual Environment
│   └── app/             <-- Source Code
│       ├── main.py
│       └── ...
└── frontend/            <-- (Future) React / Vue / Next.js 

```

---

## Tech Stack

- **Framework:** FastAPI  
- **Database:** PostgreSQL 18 (Port 1739)  
- **ORM:** SQLAlchemy  
- **Language:** Python 3  

---

## Setup & Installation

### 1. Prerequisites
- Python 3.10+ installed  
- PostgreSQL 18 installed and running  
- Database `knowyourrole` created  

---

### 2. Environment Configuration

Create a `.env` file inside the `backend/` directory:

```

DB_PASSWORD=your_actual_password_here

```

---

### 3. Installation

Open your terminal and navigate to the backend folder:

```

cd backend

```

Create a virtual environment:

```

python -m venv venv

```

Activate the virtual environment (Windows):

```

.\venv\Scripts\activate

```

Install dependencies:

```

pip install -r requirements.txt

```

---

## Running the Server

Make sure you are inside the `backend/` directory and your virtual environment is active:

```

uvicorn app.main:app --reload

```

- **API Base URL:** http://127.0.0.1:8000  
- **Interactive Documentation:** http://127.0.0.1:8000/docs  

---

## Key Features

- **Job Roles:** Create and view job roles  
- **Skills:** Create and view technical skills  
- **Architecture:** 3-Layer Pattern  
  - Router  
  - CRUD  
  - Model  
```
