# ---------- Fase 1: dependencias ----------
FROM python:3.11-slim AS dependencies

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# ---------- Fase 2: ejecución ----------
FROM python:3.11-slim

WORKDIR /app

# Copiamos las dependencias ya instaladas
COPY --from=dependencies /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=dependencies /usr/local/bin /usr/local/bin

# Copiamos el código de la aplicación
COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
