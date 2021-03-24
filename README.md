# project_management_api

A simple project management api built with django and django-rest-framework


# schema

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