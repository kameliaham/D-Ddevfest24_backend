
# Project Name: Smart Analytics Platform for Car Manufacturing Operations

## Description
This project allows you to authenticate, and retrieve data from webhooks every 20 seconds about your machines. The platform is scalable, allowing you to add machines and machine types without extensive code changes. It is developed with Django.

The project contains 4 Django apps:

1. **user (authentication)**:  
   - Admins can add managers. 
   - Managers can add operators by generating usernames and passwords randomly.
   - When an operator authenticates for the first time, they are required to change the password and provide additional information.

2. **machine**:  
   - Fetches data from webhooks every 20 seconds to save in the database (`datamachine` model). 
   - If the data is updated, a new instance is saved.
   - Data is sent to the front end via WebSockets, with Redis-server handling WebSocket communication.

3. **tasks**:  
   - This app triggers tasks when monitoring detects the need for machine maintenance or similar issues.
   - Tasks are sent to both **managers** and **operators** working on the affected machine.
   - Tasks go through a status workflow: **Not Started**, **In Progress**, and **Finished**.
   - **Managers** and **operators** can change the status of the tasks.

4. **alerts**: 
   - The alers system is triggered in two key cases:
     1. When monitoring detects a machine problem, such as exceeding a threshold (e.g., temperature).
     2. When a machine issue, such as low battery, is detected.
   - Alertss are visible to both **managers** and **operators** working on the affected machine.
   - Only **managers** can mark the notification as 'done'.
   - The notification system is managed using `GenericAPIView`.


## Setup Instructions

### 1. Install Dependencies

- pip install -r requirements.txt

Make sure you have the following dependencies installed:

- Python 3.x
- Django
- Redis (in Docker)
- Docker
- Ngrok

### 2. Subscribe to Webhooks
To subscribe to all machine webhooks:

1. Connect to Ngrok to expose your local server:

```bash
ngrok http 8000
```

You will get a URL like:
```
Forwarding https://c02a-154-121-29-131.ngrok-free.app -> http://localhost:8000
```

2. In `services.py`, update the `subscribe_all_machines()` function with your Ngrok URL (e.g., `https://c02a-154-121-29-131.ngrok-free.app`) as the callback URL.

3. Create the machines in your local environment by running:
   - `python manage.py loaddata machine/fixtures/machines.json`

### 3. Set Up Redis Server on Docker
To run Redis in a Docker container, use the following command:

```bash
docker run -d --name redis-server -p 6379:6379 redis
```

If the Redis server is already stopped, you can start it using:

```bash
docker start redis-server
```

### 4. Run the Django Project
To run the Django project locally, use:

```bash
python manage.py runserver
```

However, to handle data externally, run the project with Daphne:

```bash
daphne -b 127.0.0.1 -p 8000 backend.asgi:application
```
