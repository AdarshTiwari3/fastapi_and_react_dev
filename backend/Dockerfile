FROM python:3.12-slim

#this will bundle it in small size
ENV PYTHONDONTWRITEBYTECODE=1 
# this will log the print correctly
ENV PYTHONUNBUFFERED=1 

WORKDIR /app

COPY pyproject.toml uv.lock /app/

RUN pip install --upgrade pip
RUN pip install uv 

RUN uv sync

#copy remaining code to /app

COPY src/ /app/src

EXPOSE 8000

CMD ["sh", "-c", "uv run uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload"]
