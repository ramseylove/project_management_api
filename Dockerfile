# Pull base image
FROM python:3.8-slim-buster

ENV PATH="/scripts:${PATH}"

# Create and Set working directory
RUN useradd app -m -d /app

# Production user with limited permissions
# RUN useradd app -m -d /app \
#    && chmod -R 755 /app

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


#COPY requirements.txt .
# Copy project
COPY . /app/

RUN pip install -r reqs/requirements-dev.txt

RUN chmod +x /app/scripts/*

## Copy project
#COPY . .

##run in container as app user
USER app

ENTRYPOINT ["scripts/entrypoint.sh"]

# production server run command should probably be in entrypoint script
# CMD gunicorn config.wsgi:application --bind 0.0.0.0:$PORT
