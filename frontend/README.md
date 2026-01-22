# Frontend Assessment – To-Do Application with Next.js

## 📌 Overview

This assessment evaluates your **frontend engineering skills**. You'll build a production-ready todo application with authentication, advanced state management, optimistic updates, comprehensive error handling, and testing.

**Key Focus Areas**:

- Next.js App Router with server & client components
- Authentication flow and protected routes
- Global state management (Context API)
- Optimistic UI updates and error handling
- Form validation and user feedback
- E2E testing
- Performance optimization and accessibility
- Responsive design with Tailwind CSS

---

## ⚙️ Getting Started

### Prerequisites

- Node.js (v22 or later)
- Backend API running on `http://localhost:8000`

### Install dependencies

```bash
npm install
```

### Environment Setup

Create a `.env.local` file:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1
```

### Start dev server

```bash
npm run dev
```

Visit [http://localhost:3000](http://localhost:3000)

---

## ✅ Required Tasks

### Task 1: Authentication System

**Pages**: `/login`, `/register`

Implement complete authentication:

- [ ] Registration page with form validation
  - Email validation (proper format)
  - Password strength indicator
  - Confirm password matching
  - Display validation errors
- [ ] Login page
  - Email and password fields
  - Error handling for invalid credentials
- [ ] JWT token management
  - Store tokens securely (httpOnly cookies or localStorage with XSS protection)
  - Handle token expiration gracefully
- [ ] Protected routes
  - Redirect to login if not authenticated
  - Middleware or HOC for route protection
- [ ] User profile display
  - Show logged-in user info in header
  - Logout functionality

### Task 2: Todo Management

Build comprehensive todo interface:

#### List View

- [ ] Display todo stats of authenticated user
- [ ] Display all todos and paginated (20 per page)
- [ ] Filtering by:
  - Category (dropdown/chips)
  - Priority (HIGH, MEDIUM, LOW)
  - Completion status
  - Due date range
- [ ] Search by title functionality (debounced, min 2 chars)
- [ ] Sorting options (created_at, due_date, priority) supporting both asc and desc
- [ ] Empty states with helpful messages
- [ ] Skeleton loaders during fetch
- [ ] Infinite scroll or pagination controls

#### Todo Item Features

- [ ] View todo details (only owner)
- [ ] Quick complete/uncomplete toggle (only owner)
- [ ] Editing capability (only owner)
- [ ] Delete with confirmation modal (only owner)
- [ ] Visual indicators for:
  - Priority level (colors/badges)
  - Overdue todos
  - Category tags
- [ ] Batch operations (select multiple, bulk delete) (only owner)

#### Create/Edit Forms

- [ ] Modal or slide-over for todo creation
- [ ] Form fields:
  - Title (required, max 200 chars)
  - Description (textarea, optional)
  - Priority selector
  - Category input (autocomplete with existing)
  - Due date picker
- [ ] Real-time validation
- [ ] Cancel and save actions
- [ ] Form dirty state handling (warn before leaving)

### Task 3: Optimistic Updates & Error Handling

Implement production-ready UX patterns:

#### Optimistic Updates

- [ ] Immediately update UI when user takes action
- [ ] Show pending state (e.g., opacity, spinner)
- [ ] Rollback on error
- [ ] Re-fetch on error recovery

#### Error Handling

- [ ] Error boundaries for React errors
- [ ] API error handling with retry logic
- [ ] Network error detection (offline mode)
- [ ] Toast notifications for success/error
- [ ] Form validation errors displayed inline
- [ ] 404 page for invalid routes
- [ ] Graceful degradation

#### Loading States

- [ ] Skeleton screens for initial load
- [ ] Button loading spinners
- [ ] Progress indicators for long operations
- [ ] Suspense boundaries

### Task 4: Component Architecture

**Directory**: `components/`

Build reusable, well-structured components:

Component Requirements:

- [ ] TypeScript using `type` for all props
- [ ] Proper prop validation
- [ ] Accessible (ARIA labels, keyboard navigation)
- [ ] Responsive design
- [ ] No comments
- [ ] Composable and reusabl

### Task 5: Testing

Implement comprehensive test suite:

#### E2E Tests (Playwright)

Test scenarios:

- [ ] User registration and login flow
- [ ] Create, edit, delete todos
- [ ] Filtering and searching
- [ ] Pagination
- [ ] Error scenarios (network failure, auth errors)

**Target**: 70%+ code coverage

### Task 6: Performance Optimization

- [ ] Implement code splitting (dynamic imports)
- [ ] Lazy load components
- [ ] Debounce search input
- [ ] Throttle scroll events
- [ ] Use Next.js server components where appropriate
- [ ] Memoize expensive computations (optional)
- [ ] Prevent unnecessary re-renders (optional)
- [ ] Implement virtual scrolling for large lists (optional)

### Task 7: Accessibility & UX

- [ ] Semantic HTML throughout
- [ ] ARIA labels and roles
- [ ] Keyboard navigation support (Tab, Enter, Escape)
- [ ] Focus management (modals, forms)
- [ ] Screen reader friendly
- [ ] Color contrast meets WCAG AA standards
- [ ] Loading announcements for screen readers
- [ ] Error announcements
- [ ] Mobile-friendly touch targets

### Task 8: Responsive Design

Using Tailwind CSS:

- [ ] Mobile-first approach
- [ ] Responsive navigation (hamburger menu on mobile)
- [ ] Adaptive layouts (grid/flex)
- [ ] Touch-friendly controls on mobile
- [ ] Work on multiple device sizes

---

## 🚀 Bonus Points

- [ ] Dark mode toggle
- [ ] Internationalization (i18n)

---

## ✅ Submission Checklist

Before submitting:

- [ ] All features implemented and working
- [ ] Tests written and passing (`npm test`, `npm run test:e2e`)
- [ ] No TypeScript errors (`npm run type-check`)
- [ ] No linting errors (`npm run lint`)
- [ ] Responsive on mobile, tablet, desktop
- [ ] Accessible (keyboard navigation, screen reader)
- [ ] README updated with setup instructions
- [ ] `.env.example` included
- [ ] Code is well-documented and formatted

---

**Good luck!** Build something you'd be proud to show in a production environment. 🚀
