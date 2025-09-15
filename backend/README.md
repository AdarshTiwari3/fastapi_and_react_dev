# 🚀 FastAPI Starter with uv

A modern FastAPI backend project using:

- ⚙️ **uv** as the package manager and virtual environment handler
- ✅ **Pydantic** for request/response data validation
- 🔐 **PyJWT** for JWT-based authentication
- 🔑 **passlib[bcrypt]** for secure password hashing
- 🗃️ **SQLAlchemy** for ORM and database interaction

---

## 📦 Requirements

- Python 3.11+
- [uv](https://github.com/astral-sh/uv) package manager

### Install `uv`

```bash
# Recommended install script (Linux/macOS)
curl -LsSf https://astral.sh/uv/install.sh | sh
```

# Or via pip (if needed)

pip install uv

### Install packages

uv add <package_name>
uv add fastapi

### To remove a package

uv remove <package_name>

### To run the application

uv run uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload"
