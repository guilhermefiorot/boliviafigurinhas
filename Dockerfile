FROM python:3.11-slim AS base

WORKDIR /app

COPY requirements.txt requirements.txt

# Instalar as dependências globalmente
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8080

ENV FLASK_APP=run.py

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "run:app"]

LABEL org.opencontainers.image.source https://github.com/guilhermefiorot/boliviafigurinhasbackend