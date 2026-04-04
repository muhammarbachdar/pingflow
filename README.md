# PingFlow 🔔

A production-ready multi-channel notification engine built with FastAPI, Celery, and Redis.

## Architecture
Client → FastAPI → Redis Queue → Celery Worker → Email/Webhook
## Tech Stack

- **FastAPI** — Async REST API framework
- **PostgreSQL** — Primary database with async SQLAlchemy 2.0
- **Redis** — Message broker for Celery task queue
- **Celery** — Distributed task queue for background processing
- **Docker Compose** — Container orchestration (4 services)
- **Alembic** — Database migrations
- **JWT** — Authentication

## Features

- 🔐 JWT Authentication (register & login)
- 📨 Multi-channel notifications (email & webhook)
- ⚡ Async background processing with Celery + Redis
- 🔄 Automatic retry on failure (max 3 retries)
- 📋 Notification status tracking (pending → sent/failed)
- 🧪 Unit tested with pytest (7 tests passing)
- 🐳 Fully containerized with Docker Compose

## Getting Started

### Prerequisites
- Docker Desktop
- Git

### Run Locally
```bash
git clone https://github.com/muhammarbachdar/pingflow.git
cd pingflow
cp .env.example .env
docker-compose up --build
```

API will be available at `http://localhost:8000`
Swagger docs at `http://localhost:8000/docs`

## API Endpoints

### Auth
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /auth/register | Register new user |
| POST | /auth/login | Login & get JWT token |

### Notifications
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /notifications/ | Create notification (auth required) |
| GET | /notifications/ | Get all notifications (auth required) |

### Health
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /health | Health check |

## Running Tests
```bash
docker-compose exec app pytest tests/ -v
```

## Project Structure
```
pingflow/
├── app/
│   ├── api/
│   │   └── routes/        # API endpoints
│   ├── core/
│   │   ├── config.py      # Settings from .env
│   │   └── database.py    # Async DB setup
│   ├── models/            # SQLAlchemy models
│   ├── schemas/           # Pydantic schemas
│   ├── services/          # Business logic
│   └── workers/           # Celery tasks
├── tests/                 # Pytest test suite
├── migrations/            # Alembic migrations
├── docker-compose.yml
├── Dockerfile
└── requirements.txt
```