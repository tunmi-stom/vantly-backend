# Vantly — Personal Research and Intelligence Assistant

**Your vantage point for information, research and intelligence.**

Vantly is a personal research and intelligence assistant designed to help users discover, curate, organise and understand information about topics they care about.

Through its Telegram interface, Vantly aims to simplify information discovery and research by collecting relevant information, summarising useful findings and eventually monitoring selected topics to deliver meaningful updates.

**Live Bot:** [@vantly_bot](https://t.me/vantly_bot)

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Environment Variables](#environment-variables)
- [Running Locally](#running-locally)
- [API Documentation](#api-documentation)
- [Deployment](#deployment)
- [Versioning](#versioning)
- [Contributing](#contributing)

---

## Overview

Vantly is built around the idea of giving users an advantage when researching subjects, exploring interests or keeping up with relevant information.

Rather than spending hours manually searching through different sources, users can interact with Vantly through Telegram to discover and access useful information.

The application initially uses Telegram as its primary user interface, while a modular backend handles application logic, authentication, data management, information processing and external integrations.

Vantly is being developed with scalability, maintainability, reliability and security in mind.

## Features

### Current Capabilities

- Telegram Bot API integration.
- Webhook-based communication.
- Initial Telegram command handlers.
- Backend API infrastructure.
- Persistent database integration.
- Environment-based configuration.
- Modular application architecture.

### Planned Capabilities

- Topic discovery and research.
- Intelligent information summarisation.
- Personalised information curation.
- Continuous topic monitoring.
- Automated delivery of relevant updates.
- Additional integrations and user interfaces.

*Planned capabilities are subject to development and may change.*

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming language |
| FastAPI | Backend API framework |
| PostgreSQL | Relational database |
| SQLAlchemy | Database ORM |
| Alembic | Database migration tooling |
| HTTPX | Asynchronous HTTP communication |
| Telegram Bot API | Telegram integration |
| Neon | Managed PostgreSQL hosting |
| Railway | Backend deployment target |
| Git | Version control |
| GitHub | Source code hosting and collaboration |

## Architecture

Vantly follows a modular backend architecture designed to separate application responsibilities.

Its major components include:

1. **Telegram Interface:** Handles interactions between users and the Telegram Bot API.
2. **Webhook Layer:** Receives and validates incoming Telegram updates.
3. **Application Layer:** Coordinates application operations and business logic.
4. **Service Layer:** Contains reusable application services and processing logic.
5. **Authentication Layer:** Handles authentication and token-related operations.
6. **Database Layer:** Manages persistent data through SQLAlchemy and PostgreSQL.
7. **Core Infrastructure:** Provides shared configuration, database connections, HTTP clients and application lifecycle management.

This separation makes it easier to extend Vantly without tightly coupling its business logic to Telegram.

## Project Structure

The following is a simplified representation of the current backend organisation.

```text
vantly-backend/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── lifespan.py
│   │
│   ├── auth/
│   ├── core/
│   ├── interfaces/
│   ├── models/
│   ├── schemas/
│   └── services/
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

*The structure is illustrative. Refer to the repository for the complete and most up-to-date file listing.*

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python version supported by the project dependencies.
- Git.
- PostgreSQL or access to a Neon PostgreSQL database.
- A Telegram bot token obtained through BotFather.

### Clone the Repository

```bash
git clone https://github.com/tunmi-stom/vantly-backend.git

cd vantly-backend
```

### Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

On Linux/macOS:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root.

Use the following template:

```env
DATABASE_URL=your-database-url

JWT_SECRET=your-secret
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_DELTA=your-configured-value

TG_BOT_TOKEN=your-telegram-bot-token
TG_BOT_WEBHOOK_URL=your-webhook-url
WEBHOOK_SECRET=your-webhook-secret
```

Replace the placeholder values with your actual configuration.

**Security considerations:**

- Never commit your `.env` file.
- Keep `.env.example` free of real credentials.
- Use separate credentials for development and production.
- Store production secrets in your deployment platform's environment variable manager.
- Rotate credentials immediately if they are exposed.

## Running Locally

Start the FastAPI application using Uvicorn:

```bash
uvicorn app.main:app --reload
```

The application will normally be available at:

```text
http://127.0.0.1:8000
```

Access the API documentation at:

```text
http://127.0.0.1:8000/docs
```

## API Documentation

Vantly uses FastAPI's automatic OpenAPI documentation generation.

When enabled, the documentation is available through:

| Resource | Endpoint |
|---|---|
| Swagger UI | `/docs` |
| ReDoc | `/redoc` |
| OpenAPI Schema | `/openapi.json` |

These endpoints are useful for exploring available API routes and understanding their request and response structures.

## Deployment

Vantly's backend is designed to run as a continuously available web service.

The deployment architecture consists of:

- **Backend Hosting:** Railway.
- **Database Hosting:** Neon PostgreSQL.
- **Source Code Management:** GitHub.
- **User Interface:** Telegram.

The production deployment uses the `main` branch, while `develop` is reserved for integration and testing.

Deployment credentials and environment variables are managed independently for development and production environments.

## Versioning

Vantly follows [Semantic Versioning](https://semver.org/) using the `MAJOR.MINOR.PATCH` format.

### Current Release

**v0.1.1 — Initial Start and Help Commands**

This release introduces the initial `/start` and `/help` command handlers.

### Release History

Release notes and version history are available through the repository's [GitHub Releases](https://github.com/tunmi-stom/vantly-backend/releases) page.

## Contributing

Contributions, suggestions and bug reports are welcome.

If you would like to contribute:

1. Fork the repository.
2. Create a feature branch from `develop`.
3. Implement your changes.
4. Test your implementation.
5. Submit a pull request targeting `develop`.

Example:

```bash
git checkout develop

git pull origin develop

git checkout -b feature/your-feature
```

Please keep contributions focused, maintain readable code and follow the existing project conventions.

---

**Vantly — Your vantage point for information.**