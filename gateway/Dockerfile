FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY config/ ./config/
COPY chemistry/ ./chemistry/
COPY infrastructure/chemicals_hormones/ ./infrastructure/chemicals_hormones/
COPY gateway/ ./gateway/

CMD ["uvicorn", "gateway.main:app", "--host", "0.0.0.0", "--port", "8000"]