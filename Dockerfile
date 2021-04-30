# Pull base image
FROM python:3.8-slim-buster

# Create and Set working directory
RUN useradd app -m -d /app \
    && chmod -R 755 /app

WORKDIR /app

#expoose the port for dokku
EXPOSE 8000

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8000

RUN apt-get update \
    && apt-get install gcc python3-dev libpq-dev -y  \
    && pip install --upgrade pip \
    && apt-get clean


COPY requirements.txt .

RUN pip install -r requirements.txt

# Copy project
COPY . .

RUN ./manage.py collectstatic --noinput

##run in container as unpriviliged app user
USER app

CMD gunicorn config.wsgi:application --bind 0.0.0.0:$PORT
