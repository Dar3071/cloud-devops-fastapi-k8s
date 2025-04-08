# FastAPI with Docker and PostgreSQL

This project showcases skills in building a FastAPI web application with Docker and PostgreSQL. I used:
- **FastAPI** for building a fast and modern API.
- **Docker** for containerizing the app and PostgreSQL database.
- **PostgreSQL** for data storage and integration.
- **pytest** for automated testing to ensure functionality.

The project demonstrates web development, containerization, and database integration best practices.


## Features
- FastAPI backend
- PostgreSQL database
- Dockerized development environment
- Health check endpoint (`/health`)

## Prerequisites
- Docker
- Docker Compose

## Getting Started
```bash
## 1. Clone the Repository

git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name

## 2. Build and Start the Containers

docker-compose up --build
This will build the Docker images and start the application along with the PostgreSQL container.

## 3. Access the Application
Once the containers are up and running, you can access the FastAPI application at:

http://localhost:8000
You can also check the health endpoint:

http://localhost:8000/health
## 4. Run Tests
To run tests using pytest, use:

docker-compose run test

## Project Structure

├── app
│   ├── db.py
│   ├── main.py
│   ├── requirements.txt
│   └── __pycache__
├── docker-compose.yml
├── Dockerfile
├── tests
│   └── test_main.py
└── README.md

## Environment Variables
POSTGRES_USER: PostgreSQL username (default: devuser)

POSTGRES_PASSWORD: PostgreSQL password (default: devpass)

POSTGRES_DB: PostgreSQL database name (default: devdb)

## Built With

FastAPI

PostgreSQL

Docker
