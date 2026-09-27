# Appointment Management API

A robust, production-ready RESTful API built with **FastAPI**, **SQLAlchemy ORM**, and **Pydantic v2**. This project follows modular software architecture patterns (`APIRouter`) and implements automated database persistence with SQLite.

## 🚀 Live Demo
The API is automatically deployed and accessible live at:
[https://onrender.com](https://onrender.com) *(Replace with your actual link if needed)*

## 🛠️ Tech Stack & Key Features
- **FastAPI:** High-performance, asynchronous web framework for Python.
- **SQLAlchemy ORM:** Relational database mapping with explicit session lifecycles.
- **Pydantic V2:** Enterprise-grade data validation and schema settings.
- **Pytest:** Structured suite of automated unit and integration tests.
- **Architecture:** Clean, modular routing organization using `APIRouter`.

## 📁 Project Structure
```text
├── routers/
│   ├── clientes.py       # Customer CRUD operations
│   └── agendamentos.py   # Appointment scheduling logic
├── database.py           # Database connection & session management
├── models.py             # SQLAlchemy database tables mapping
├── schemas.py            # Pydantic data validation schemas
├── test_main.py          # Automated integration tests
└── main.py               # Application entrypoint & initializations
```

## ⚙️ How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com
cd api-agendamento-fastapi
```

### 2. Set up Virtual Environment
```bash
python -m venv venv
source venv/Scripts/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the development server
```bash
uvicorn main:app --reload
```
Access the interactive documentation locally at `http://localhost:8000/docs`.

## 🧪 Running Automated Tests
The application includes integrated test cases that run on an isolated in-memory SQLite instance:
```bash
python -m pytest -v
```

##### Developed By Jorge Santos ####