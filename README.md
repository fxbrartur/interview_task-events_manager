# Event Management System

This project is an event management system developed with Django Rest Framework (DRF). It allows the creation, update, deletion, and listing of event information, as well as the creation, update, and removal of users for event participation and notifications about event updates.

## Features

1. User CRUD
2. Event CRUD
3. Participant Registration
4. Notifications for Participants
5. Reports

## Requirements

- Python 3.12
- Django 5.0.6
- Django Rest Framework 3.15.2
- DRF-Spectacular 0.27.2
- Celery 5.4.0
- Redis 5.0.6
- Pillow 10.3.0

## Environment Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/fxbrartur/freelaw_events_manager.git
cd freelaw_events_manager
```

### Step 2: Create and Activate the Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```
### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

Ensure that the dependencies are compatible with your local environment, otherwise adapt as necessary.

### Step 4: Configure the Database

Edit the settings.py file to configure your database if necessary. The project is configured to use SQLite by default as provided by Django.

### Step 5: Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Initialization and Testing

Ensure that Redis is running on port 6379:
```bash
redis-server
```

In a new tab, run the Development Server:
```bash
python manage.py runserver
```

In a new tab, start the Celery worker:
```bash
celery -A events_manager worker --loglevel=info
```

In a new tab, run the tests to ensure everything is installed and initialized correctly:
```bash
pytest
```

## Using the API

##### POST /api/users/ - To start, first create a user:
``` bash
curl -X 'POST' \
  'http://localhost:8000/api/users/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "example",
  "email": "example@example.com",
  "first_name": "example",
  "last_name": "example",
  "password": "example",
  "image_url": "https://avatars.githubusercontent.com/u/89175768?v=4"
}'
```
Expected output example:
``` bash
{
  "id": 3,
  "username": "cvyHOpOsPoBrmA.guNhtZkXjvgdT7wTbxI7yfziUFSi@NaXB",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "created_at": "2024-05-22T23:16:39.561918Z",
  "token": "<seu_token_aqui>"
}
```
The generated token will be used in the header for authorization of requests in the other endpoints.

## API Documentation

### Swagger
The interactive API documentation can be accessed via Swagger at the following URL: http://localhost:8000/api/schema/swagger-ui/

### Available Endpoints

The API provides the following endpoints:

#### Eventos: 

<details>
  <summary>GET /api/events/ - List all available events</summary>

Example request:
``` bash
curl -X 'GET' \
  'http://localhost:8000/api/events/' \
  -H 'accept: application/json' \
  -H 'Authorization: Token <seu_token_aqui>'
```

Expected output example:

``` bash
[
  {
    "id": 2,
    "title": "string",
    "description": "string",
    "date": "2024-06-21",
    "time": "20:01:00",
    "location": "ali",
    "created_at": "2024-06-20T21:49:28.119172Z",
    "updated_at": "2024-06-21T16:07:16.073321Z"
  },
  {
    "id": 3,
    "title": "Test",
    "description": "test",
    "date": "2025-06-22",
    "time": "20:21:00",
    "location": "acula",
    "created_at": "2024-06-20T21:49:41.620780Z",
    "updated_at": "2024-06-20T21:52:19.406385Z"
  }
]
```
</details>

<details>
  <summary>POST /api/events/ - Create a new event</summary>

Example request:
``` bash
curl -X 'POST' \
  'http://localhost:8000/api/events/' \
  -H 'accept: application/json' \
  -H 'Authorization: Token <seu_token_aqui>' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "string",
  "description": "string",
  "date": "2024-06-21",
  "time": "20:21",
  "location": "string"
}'
```

Expected output example:

``` bash
{
  "id": 5,
  "title": "string",
  "description": "string",
  "date": "2024-06-21",
  "time": "20:21:00",
  "location": "string",
  "created_at": "2024-06-21T16:25:24.533303Z",
  "updated_at": "2024-06-21T16:25:24.533326Z"
}
```

</details>

<details>
  <summary>GET /api/events/{id}/ - Retrieve information about a specific event</summary>

Example request:
``` bash
curl -X 'GET' \
  'http://localhost:8000/api/events/1/' \
  -H 'accept: application/json' \
  -H 'Authorization: Token <seu_token_aqui>'
```

Expected output example:
``` bash
{
  "id": 1,
  "title": "Evento Teste",
  "description": "Descrição do evento",
  "date": "2024-06-22",
  "time": "15:00:00",
  "location": "Local do evento",
  "created_at": "2024-06-20T20:00:00.000000Z",
  "updated_at": "2024-06-21T15:00:00.000000Z"
}
```
</details>

<details>
  <summary>PUT /api/events/{id}/ - Update a specific event</summary>

Example request:
```bash
curl -X 'PUT' \
  'http://localhost:8000/api/events/2/' \
  -H 'accept: application/json' \
  -H 'Authorization: Token <seu_token_aqui>' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "string",
  "description": "string",
  "date": "2024-04-24",
  "time": "20:01",
  "location": "local1"
}'
```

Expected output example:
``` bash
{
  "id": 2,
  "title": "string",
  "description": "string",
  "date": "2024-06-21",
  "time": "20:01:00",
  "location": "local1",
  "created_at": "2021-03-03T21:49:28.119172Z",
  "updated_at": "2024-04-24T16:32:11.832852Z"
}
```

</details>

<details>
  <summary>DELETE /api/events/{id}/ - Delete a specific event</summary>

Example request:
```bash
curl -X 'DELETE' \
  'http://localhost:8000/api/events/3/' \
  -H 'accept: */*' \
  -H 'Authorization: Token <seu_token_aqui>' \
```

Expected output example:
``` bash
status = 204 - No response body
```

</details>

<details>
  <summary>GET /api/events/{id}/report/ - Generate a report for a specific event</summary>

Example request:
```bash
curl -X 'GET' \
  'http://localhost:8000/api/events/4/report/' \
  -H 'accept: application/json' \
  -H 'Authorization: Token <seu_token_aqui>'
```
Expected output example:
``` bash
{
  "event": "event1",
  "participant_count": 2,
  "participants": [
    {
      "first_name": "ela",
      "last_name": "dela",
      "email": "nela@example.com",
      "image": ""
    },
    {
      "first_name": "ele",
      "last_name": "dele",
      "email": "nele@example.com",
      "image": "profile_pics/156056254v4"
    }
  ]
}
```

</details>

<details>
  <summary>POST /api/events/{id}/subscribe/ - Allow users to subscribe to events</summary>

Example request:
```bash
curl -X 'POST' \
  'http://localhost:8000/api/events/2/subscribe/' \
  -H 'accept: application/json' \
  -H 'Authorization: Token <seu_token_aqui>>' \
  -d ''
```

Expected output example:
``` bash
{
  "status": "subscribed"
}
```

</details>

#### Users:

<details>
  <summary>GET /api/users/ - Retrieve information from the logged user</summary>

Example request:
```bash
curl -X 'GET' \
  'http://localhost:8000/api/users/' \
  -H 'accept: application/json' \
  -H 'Authorization: Token <seu_token_aqui>'
```

Expected output example:
``` bash
[
  {
    "id": 3,
    "username": "cvyHOpOsPoBrmA.guNhtZkXjvgdT7wTbxI7yfziUFSi@NaXB",
    "email": "user@example.com",
    "first_name": "string",
    "last_name": "string",
    "created_at": "2024-03-11T11:56:39.561918Z",
    "token": "<seu_token_aqui>"
  }
]
```
</details>  
<details>
  <summary>POST /api/users/ - Create a new user</summary>

Example request:
``` bash
curl -X 'POST' \
  'http://localhost:8000/api/users/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "example",
  "email": "example@example.com",
  "first_name": "example",
  "last_name": "example",
  "password": "example",
  "image_url": "https://avatars.githubusercontent.com/u/89175768?v=4"
}'
```

Expected output example:
``` bash
{
  "id": 3,
  "username": "cvyHOpOsPoBrmA.guNhtZkXjvgdT7wTbxI7yfziUFSi@NaXB",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "created_at": "2023-02-11T23:16:39.561918Z",
  "token": "<seu_token_aqui>"
}
```
The generated token will be used in the header for authorization of requests in the other endpoints.
</details>  

<details>
  <summary>GET /api/users/{id}/ - Retrieve information about a specific event</summary>
Administrative endpoint, for a superadmin to manage the software's users in a near future:

Example request:
```bash
curl -X 'GET' \
  'http://localhost:8000/api/users/3/' \
  -H 'accept: application/json' \
  -H 'Authorization: Token <seu_token_aqui>'
```

Expected output example:

```bash
{
  "id": 3,
  "username": "cvyHOpOsPoBrmA.guNhtZkXjvgdT7wTbxI7yfziUFSi@NaXB",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "created_at": "2023-02-11T23:16:39.561918Z",
  "token": "<seu_token_aqui>"
}
```

</details>  

<details>
  <summary>PUT /api/users/{id}/ - Update a specific event</summary>

Example request:
```bash
curl -X 'PUT' \
  'http://localhost:8000/api/users/3/' \
  -H 'accept: application/json' \
  -H 'Authorization: Token <seu_token_aqui>' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "123",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "password": "string"
}'
```

Expected output example:

```bash
{
  "id": 3,
  "username": "123",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "created_at": "2024-06-21T14:56:39.561918Z",
  "token": <seu_token_aqui>
}
```

</details>  

<details>
  <summary>DELETE /api/users/{id}/ - Delete a specific event</summary>

Example request:
```bash
curl -X 'DELETE' \
  'http://localhost:8000/api/users/3/' \
  -H 'accept: */*' \
  -H 'Authorization: Token <seu_token_aqui>' \
```

Expected output example:
```bash
status = 204 - No response body
```

</details>  

## Notes

- For microservices, I implemented everything that I considered to be heavier in real life and also what did not need immediate response. Those are: Event Reports Generation, Event Subscription Confirmation, and Event Update Notifications. Notifications and confirmations are represented by prints in the Celery worker log, but in a real scenario, we would switch this to an SMTP (or something else), which I have already pre-configured in settings.py.

<br>

- Providing only examples of successful output so that the documentation does not become too large, but yes, I have implemented some ERROR HANDLING situations.

<br>

- With more time, I would configure user permissions, where I would bring a more realistic behavior, such as each user owning the event they created, where only they can edit and delete their own event, or when deleted and/or edited by another it would generate an approval request.
