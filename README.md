# project_management_api

A simple project management api built with django and django-rest-framework

## Not ready for production use, permission system broke with django guardian change

###Built with:
* Docker and Docker-Compose
* Makefile
* Postgres 11
* django storages and boto3 - implemented with Digital Oceans Spaces
* djoser 2.x - REST implementation of Django authentication system
* drf-yasg - Generate real Swagger/OpenAPI 2.0 specs
 

# Getting started
1. create env file named dev.env in /envs folder
2. Define these variables in dev.env

SECRET_KEY= \
ENVIRONMENT=docker_development \
DEBUG=1 \
ALLOWED_HOSTS=127.0.0.1,localhost,0.0.0.0 \

AWS_ACCESS_KEY_ID= \
AWS_SECRET_ACCESS_KEY= \
USE_S3= 

DB_USER=postgres \
DB_PORT=5432 \
DB_HOST=db

3. run `make up`

# Schema

## Custom User

- *UserRole → choices*
    - admin
    - manager
    - developer
    - client
- client_id

## client
- id
- name

## Project
- id
- key (3-4 char)
- name
- description
- project_priority → choices
    - low
    - medium
    - high
- project_status → choices
    - planning
    - in-progress
    - in-review
    - finished
- user_id

## Issue

- id
- key (project key + int i.e. proj-1)
- summary
- description
- created_at
- updated_at
- Issue_status → choices
    - to-do
    - in-progress
    - done
- issue_priority → choices
    - low
    - medium
    - high
- issuetype → choices
    - task
    - bug
    - story
- **project_id**

## IssueImage
- id
- filename
- content
- thumbnail
- image
- **issue_id**

## Comments
- user_id
- comment
- created_at
- update_at