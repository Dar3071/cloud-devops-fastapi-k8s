# cloud-devops-fastapi-k8s

FastAPI Project with Docker & PostgreSQL

Overview
This project is a simple FastAPI application running with PostgreSQL in Docker. It includes API endpoints, database interaction, and basic testing using pytest.

Features
FastAPI for building RESTful APIs

PostgreSQL for data storage

Docker for containerization

Pytest for automated testing

Prerequisites
Docker and Docker Compose installed

Python 3.12 (for development)

Getting Started
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo
Build and run the application using Docker Compose:

bash
Copy
Edit
docker-compose up --build
The application will be available at:

API: http://localhost:8000

Health check endpoint: http://localhost:8000/health

Running Tests
To run tests, use the following command:

bash
Copy
Edit
docker-compose run test
This will run pytest against the /tests directory.

Endpoints
GET /health - Check if the app is running (returns {"status": "OK"}).

Other API Endpoints - (Add any relevant API documentation here).

Technologies Used
FastAPI: For building the API.

PostgreSQL: For database storage.

Docker: For containerization.

pytest: For testing.

