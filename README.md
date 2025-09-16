# 🐳 Full-Stack App with FastAPI + React + PostgreSQL (Dockerized)

This project is a full-stack web application with:

- ⚙️ **FastAPI** (Python) backend
- 🎨 **React** frontend
- 🗄️ **PostgreSQL** database
- 🛠️ **pgAdmin** for database management
- 🐳 Managed with **Docker Compose**

---

<!-- ## 📁 Project Structure -->
<pre> ```text 📁 Project Structure
├── backend/
│ ├── src/
│ │ ├── api/
│ │ │ └── v1/
| | │ │ │ ├── auth/
| | | │ │ │ ├── controller.py
| | | │ │ │ ├── model.py
| | | │ │ │ ├── service.py
| | | │ │ │ └── utils.py
│ │ ├── config/
│ │ │ └── settings.py
│ │ ├── database/
│ │ │ └── database.py
│ │ ├── entities/
│ │ │ └── user.py
│ │ ├── main.py
│ │ └── routes.py
│ ├── Dockerfile
│ └── pyproject.toml
│
├── frontend/
│ ├── public/
│ ├── src/
│ │ ├── assets/
│ │ ├── components/
│ │ │ └── hooks/
│ │ │ └── files/
│ │ └── App.tsx
│ ├── Dockerfile
│ ├── package.json
│ └── vite.config.ts
│
├── docker-compose.yaml
├── .env
└── README.md
</pre>

---

## 🚀 Getting Started

### 🔧 Prerequisites

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- `.env` file in the root directory
- Docker must be installed on the system

---

## 📄 .env File Example

```env
# PostgreSQL
POSTGRES_USER=postgres
POSTGRES_PASSWORD=yourpassword
POSTGRES_DB=yourdb
POSTGRES_HOST=db
POSTGRES_PORT=5432

# pgAdmin
PGADMIN_DEFAULT_EMAIL=admin@example.com
PGADMIN_DEFAULT_PASSWORD=admin123
```

### To Build and run the application

docker-compose up --build
