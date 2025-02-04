FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# השתמש במשתנה סביבה PORT או בפורט ברירת מחדל 8080
CMD gunicorn "run:app" --bind "0.0.0.0:${PORT:-8080}"
