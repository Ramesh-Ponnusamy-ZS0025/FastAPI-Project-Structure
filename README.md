# 🚀 FastAPI Project

This is a **FastAPI** project with **SQLAlchemy** and **Alembic** for database migrations.

---

## 📦 Setup

### 1. Clone the repo
```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
```

### 2. Create and activate virtual environment
```bash
# Windows
python -m venv myenv
myenv\Scripts\activate

# Linux / Mac
python3 -m venv myenv
source myenv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## ⚙️ Database Setup

Update the `alembic.ini` file with your database URL:

**PostgreSQL:**
```ini
sqlalchemy.url = postgresql://username:password@localhost:5432/mydb
```

**SQLite:**
```ini
sqlalchemy.url = sqlite:///./test.db
```

---

## 🗂 Alembic Migrations

Create a new migration:
```bash
alembic revision --autogenerate -m "Describe your migration"
```

Apply migrations:
```bash
alembic upgrade head
```

Rollback last migration:
```bash
alembic downgrade -1
```

---

## ▶️ Run the App

```bash
uvicorn src.main:app --reload
```

- Open in browser → [http://127.0.0.1:8000](http://127.0.0.1:8000)  
- API Docs → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  

---

## 📁 Project Structure (example)

```
fastapi-project
├── alembic/                  # DB migrations
├── src
│   ├── auth
│   │   ├── router.py
│   │   ├── schemas.py
│   │   ├── models.py
│   │   ├── dependencies.py
│   │   ├── config.py
│   │   ├── constants.py
│   │   ├── exceptions.py
│   │   ├── service.py
│   │   └── utils.py
│   ├── posts
│   │   ├── router.py
│   │   ├── schemas.py
│   │   ├── models.py
│   │   ├── dependencies.py
│   │   ├── constants.py
│   │   ├── exceptions.py
│   │   ├── service.py
│   │   └── utils.py
│   ├── config.py
│   ├── models.py
│   ├── exceptions.py
│   ├── pagination.py
│   ├── database.py
│   └── main.py
├── tests/
│   ├── auth
│   └── posts
├── requirements/
│   ├── base.txt
│   ├── dev.txt
│   └── prod.txt
├── .env
├── logging.ini
└── alembic.ini

```

---

## ✅ Useful Commands

Check current revision:
```bash
alembic current
```

Show migration history:
```bash
alembic history
```

---

## 🛠 Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/)  
- [SQLAlchemy](https://www.sqlalchemy.org/)  
- [Alembic](https://alembic.sqlalchemy.org/)  
- [Uvicorn](https://www.uvicorn.org/)  

---

## ✨ Notes

- Always run migrations after updating models.  
- Use a `.env` file for secrets (database URL, API keys, etc.).  
- For production, disable `--reload` and use a process manager (e.g., Gunicorn + Uvicorn workers).  
