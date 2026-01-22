# Full Stack Engineering Assessment – Production TODO Application

Welcome to the Full Stack Engineering Assessment! This challenge evaluates your ability to build a **production-ready TODO application** with modern architecture patterns, authentication, database integration, and comprehensive testing.

**Estimated Time**: 2-4 hours

---

## 🎯 Objective

Build a complete, production-grade TODO application with:

- **Backend**: RESTful API using FastAPI with PostgreSQL/SQLite database, JWT authentication, and comprehensive testing
- **Frontend**: Next.js application with state management, authentication flow, optimistic updates, and error handling
- **DevOps**: Dockerized services, environment configuration, and deployment readiness

---

## 🔑 Core Requirements

### Authentication & Authorization

- [ ] User registration and login system
- [ ] JWT-based authentication
- [ ] Protected routes/endpoints
- [ ] User-specific todo access (users can only see their own todos)

### Database & Persistence

- [ ] Use a real database (PostgreSQL preferred, SQLite acceptable)
- [ ] Proper database migrations
- [ ] Efficient querying with pagination
- [ ] Database connection pooling

### Advanced Features

- [ ] Pagination and filtering on todo lists
- [ ] Search functionality
- [ ] Todo categories/tags
- [ ] Due dates and priority levels

### Testing

- [ ] Backend: Unit tests and integration tests (pytest)
- [ ] Frontend: E2E tests
- [ ] Minimum 70% code coverage

### Performance & Quality

- [ ] Input validation and sanitization
- [ ] Proper error handling and logging
- [ ] API rate limiting
- [ ] Optimistic UI updates on frontend
- [ ] Loading and error states
- [ ] Responsive design

---

## 📋 Detailed Requirements

Please check:

- [`/backend/README.md`](./backend/README.md) for detailed Backend requirements
- [`/frontend/README.md`](./frontend/README.md) for detailed Frontend requirements

---

## 🚀 Submission Requirements

### Must Include:

1. **GitHub Repository** with:
   - Clear README with setup instructions
   - `.env.example` files for both frontend and backend
   - Docker Compose configuration
2. **Documentation**:
   - API documentation
   - Architecture decisions and trade-offs
3. **Tests**:
   - Test suites for both frontend and backend
   - Instructions to run tests

4. **Working Application**:
   - Both services run independently
   - Successful frontend-backend integration
   - All features functional

### Evaluation Criteria:

- **Code Quality** (30%): Clean, maintainable, well-structured code
- **Functionality** (25%): All required features working correctly
- **Architecture** (20%): Proper separation of concerns, scalable design
- **Testing** (15%): Comprehensive test coverage
- **Security** (10%): Authentication, validation, secure practices

---

Good luck! We're excited to see your solution. 🚀

**Questions?** Contact us via invitation email and we'll respond.
