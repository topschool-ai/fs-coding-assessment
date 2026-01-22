# Backend Assessment - FastAPI Todo API with Authentication & Database

## Overview

This assessment evaluates your ability to build a **production-grade RESTful API** using FastAPI. You'll create a secure, scalable backend for a todo management system with authentication, database integration, and comprehensive testing.

**Key Focus Areas**:

- Database design and migrations (SQLModel/Alembic)
- JWT authentication and authorization
- Advanced API patterns (pagination, filtering, searching)
- Input validation and error handling
- Testing and code quality
- Security best practices

## Getting Started

### Prerequisites

- Python 3.12+
- PostgreSQL (recommended) or SQLite
- This project uses `uv` for dependency management

### Setup

1. Clone this repository
2. Create a `.env` file (see `.env.example`)
3. Install dependencies:
   ```bash
   uv sync
   ```
4. Run the development server:
   ```bash
   uv run uvicorn app.main:app --reload
   ```

The API will be available at `http://localhost:8000`

## Required Tasks

### Task 1: Database Setup & Models (SQLModel)

Create SQLModel database models (combines SQLModel + Pydantic):

- **User Model**:
  - `id`: UUID primary key
  - `email`: Unique, indexed, validated
  - `username`: Unique, indexed
  - `hashed_password`: String
  - `is_active`: Boolean (default True)
  - `created_at`: DateTime with timezone
  - `updated_at`: DateTime with timezone

- **Todo Model**:
  - `id`: UUID primary key
  - `title`: String (max 200 chars, required)
  - `description`: Text (required)
  - `completed`: Boolean (default False)
  - `priority`: Enum (LOW, MEDIUM, HIGH)
  - `due_date`: DateTime with timezone (optional)
  - `category`: String (optional, indexed)
  - `user_id`: Foreign key to User (indexed)
  - `created_at`: DateTime with timezone
  - `updated_at`: DateTime with timezone

- Request/response schemas with proper validation
- Use Pydantic V2 features (field validators, model config)
- Separate schemas for create, update, and response

### Task 2: Authentication System

Implement JWT-based authentication:

- **POST /auth/register**: Create new user
  - Email validation (must be valid email format)
  - Password strength requirements (min 8 chars, special char, number)
- **POST /auth/login**: User login
  - Return JWT access token
  - Token expiry: access (30 min)
- **GET /auth/me**: Get current user profile (protected)

### Task 3: Database Layer & Repository Pattern

Set up database connection:

- Use SQLModel with async support
- Connection pooling configuration
- Proper session management with dependency injection

### Task 4: Advanced Todo API Endpoints

All endpoints require authentication (Bearer token).

#### POST /todos

Create a new todo with validation:

#### GET /todos

Get all todos. Hide description. (Only authenticate users, and can see other todos except `description` field)

#### GET /todos/{todo_id}

Get single todo (only owner)

#### PUT or PATCH /todos/{todo_id}

Update todo (partial updates supported) (only owner)

#### DELETE /todos/{todo_id}

Delete todo (only owner)

#### PATCH /todos/{todo_id}/complete

Mark todo as complete (only owner)

#### GET /todos/stats

Get user's todo statistics: total, completed, pending, by priority (only owner)

### Task 5: Middleware & Error Handling

Implement:

- Request ID middleware (generate UUID for each request)
- Logging middleware (log request/response)
- Rate limiting (optional: use slowapi)
- Global exception handlers
- Custom error responses with proper status codes

### Task 6: Migrations & Seeding

- Set up Alembic for database migrations
- Create initial migration for User and Todo tables
- Add indexes for performance
- Create seed script with sample data

### Task 7: Testing

Implement comprehensive tests:

**Unit Tests**:

- Test utility functions (password hashing, token generation)
- Test repository methods
- Test Pydantic schema validation

**Integration Tests**:

- Test API endpoints with test database
- Test authentication flows
- Test authorization (users can't access others' todos)
- Test pagination and filtering
- Test error cases (404, 401, 422, etc.)

**Test Coverage**: Aim for 70%+ coverage

Run tests:

```bash
uv run pytest tests/ -v --cov=app --cov-report=html
```

### Task 8: API Documentation & Validation

- Leverage FastAPI's auto-generated docs (`/docs`)
- Add comprehensive docstrings to all endpoints
- Use OpenAPI tags for organization
- Add request/response examples in schemas
- Version your API (`/api/v1/...`)

## Technical Requirements

### Database

- [ ] Use SQLAlchemy 2.0+ with async support
- [ ] Implement proper migrations with Alembic
- [ ] Add database indexes for performance
- [ ] Use UUID for primary keys
- [ ] Connection pooling configured

### Authentication

- [ ] JWT tokens with proper expiration
- [ ] Secure password hashing
- [ ] Protected endpoints with dependencies
- [ ] User can only access their own todos (Note: all todos can be viewed by all authenticated users)

### API Design

- [ ] RESTful conventions followed
- [ ] Proper HTTP status codes
- [ ] Pagination for list endpoints
- [ ] Filtering and search capabilities
- [ ] Input validation with Pydantic V2
- [ ] Consistent error response format

### Code Quality

- [ ] Type hints throughout
- [ ] Proper project structure
- [ ] Environment-based configuration
- [ ] Logging configured
- [ ] PEP 8 compliance (use ruff/black)

### Testing

- [ ] Unit tests for business logic
- [ ] Integration tests for API endpoints
- [ ] Minimum 70% code coverage

## Bonus Points

- [ ] Add rate limiting with slowapi
- [ ] Add /health for checking database connection

## Submission

Ensure your submission:

1. **Runs Successfully**:

   ```bash
   uv run uvicorn app.main:app --reload
   uv run pytest tests/ -v
   ```

2. **Includes Documentation**:
   - Clear setup instructions in README
   - `.env.example` file
   - API documentation accessible at `/docs`

3. **Code Quality**:
   - Passes linting
   - Type checked
   - All tests passing

4. **Database**:
   - Migrations folder included
   - Seed data script

**Good luck!** 🚀
