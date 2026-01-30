# -------- Stage 1: Build --------
FROM python:3.11-slim AS builder

WORKDIR /app

COPY app/requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY app/ .

# -------- Stage 2: Runtime --------
FROM python:3.11-slim

WORKDIR /app

# Copy only what is needed from builder
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /app /app

ENV APP_NAME="SecureShip API"
ENV APP_VERSION="v1"
ENV ENVIRONMENT="production"

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

