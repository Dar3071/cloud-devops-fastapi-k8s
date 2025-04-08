# FastAPI with Docker and PostgreSQL

This project is a simple FastAPI application configured with Docker and PostgreSQL.

## Features
- FastAPI backend
- PostgreSQL database
- Dockerized development environment
- Health check endpoint (`/health`)

## Prerequisites
- Docker
- Docker Compose

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
2. Build and Start the Containers
bash
Copy
Edit
docker-compose up --build
This will build the Docker images and start the application along with the PostgreSQL container.

3. Access the Application
Once the containers are up and running, you can access the FastAPI application at:

arduino
Copy
Edit
http://localhost:8000
You can also check the health endpoint:

bash
Copy
Edit
http://localhost:8000/health
4. Run Tests
To run tests using pytest, use:

bash
Copy
Edit
docker-compose run test
Project Structure
css
Copy
Edit
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
Environment Variables
POSTGRES_USER: PostgreSQL username (default: devuser)

POSTGRES_PASSWORD: PostgreSQL password (default: devpass)

POSTGRES_DB: PostgreSQL database name (default: devdb)

Built With
FastAPI

PostgreSQL

Docker
