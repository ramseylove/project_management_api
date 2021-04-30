# Pull base image
FROM python:3.8-slim-buster

# Create and Set working directory
RUN mkdir /app
WORKDIR /app

#expoose the port for dokku
EXPOSE 8000

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8000

RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libc-dev python3-dev \
    && pip install --upgrade pip \
    && apt-get autoclean


COPY requirements.txt .

RUN pip install -r requirements.txt

# Copy project
COPY . .

RUN ./manage.py collectstatic --noinput
#
#RUN useradd -D app \
#    && chown +R app:app /app \
#    && chmod +R 755 /app
##run in container as unpriviliged app user
#USER app

CMD gunicorn config.wsgi:application --bind 0.0.0.0:$PORT
