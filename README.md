
# Eujim Solutions App Documentation

## 1. Project Overview

This document provides a comprehensive overview of the Eujim Solutions application, a robust platform designed to connect job seekers with recruiters. The application is built with Django and Django REST Framework, featuring distinct modules for user management, job seekers, recruiters, job postings, and more.

### Key Technologies:
- **Backend:** Django, Django REST Framework
- **Database:** MySQL
- **Asynchronous Tasks:** Celery with Redis
- **Real-time Communication:** Django Channels
- **Authentication:** JWT (JSON Web Tokens)

---

## 2. Project Structure

The project is organized into several Django apps, each responsible for a specific domain:

- `users`: Handles user authentication, registration, and profile management.
- `jobseeker`: Manages job seeker profiles, including education, certifications, and skills.
- `recruiter`: Manages recruiter profiles, including company information and document verification.
- `job_posting`: Allows recruiters to post and manage job listings.
- `job_scraper`: Periodically scrapes job listings from external sources.
- `skills`: Manages the skills that can be associated with job seekers and job postings.
- `search`: Provides search functionality across the platform.

---

## 3. Installation and Setup

### Prerequisites:
- Python 3.8+
- MySQL
- Redis

### Steps:
1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd eujimsolutionApp
   ```
2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirement.txt
   ```
4. **Configure environment variables:**
   Create a `.env` file in the root directory and add the following:
   ```
   DB_NAME=your_db_name
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password
   DB_HOST=localhost
   DEFAULT_FROM_EMAIL=your_email@example.com
   ... (add other variables as needed)
   ```
5. **Run database migrations:**
   ```bash
   python manage.py migrate
   ```
6. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

---

## 4. Application Architecture

The application follows a three-layer architecture to ensure a clean separation of concerns, making the codebase more maintainable, scalable, and testable.

### 4.1. Presentation Layer
- **Components:** `views`, `serializers`, `urls`
- **Description:** This layer is the entry point for all client interactions. It is responsible for handling HTTP requests, validating incoming data, and serializing outgoing data.
  - **Views (`/views`):** Handle the request-response cycle. They receive requests, pass data to the business logic layer, and return responses.
  - **Serializers (`/serializers`):** Validate and deserialize incoming data, and serialize complex data types (like querysets) into JSON.
  - **URLs (`/urls`):** Define the API endpoints and map them to the appropriate views.

### 4.2. Business Logic Layer
- **Components:** `services`
- **Description:** This layer contains the core application logic. It orchestrates the application's functionality by processing data, applying business rules, and coordinating between the presentation and data access layers. By encapsulating the business logic in services, the views remain lean and focused on handling HTTP-related tasks.

### 4.3. Data Access Layer
- **Components:** `models`, `repositories`
- **Description:** This layer is responsible for all interactions with the database.
  - **Models (`/models.py`):** Define the database schema and relationships between tables.
  - **Repositories (`/repository`):** Abstract the database queries, providing a clean API for the business logic layer to perform CRUD (Create, Read, Update, Delete) operations. This isolates the database logic and makes it easier to manage and test.

---

## 5. API Documentation

The API is versioned under `/api/v1/`.

### 4.1. Users API (`/api/v1/users/`)
- **Authentication:**
  - `POST /auth/register/`: Register a new user.
  - `POST /auth/login/`: Log in and receive JWT tokens.
  - `POST /auth/logout/`: Log out.
- **User Management:**
  - `GET /profile/`: Get the profile of the currently logged-in user.
  - `PUT /profile/`: Update the profile of the currently logged-in user.

### 4.2. Job Seeker API (`/api/v1/jobseeker/`)
- **Profile:**
  - `GET /profile/`: Get the job seeker's profile.
  - `PUT /profile/`: Update the job seeker's profile.
- **Education:**
  - `GET /education/`: List all education entries.
  - `POST /education/`: Add a new education entry.
- **Skills:**
  - `GET /skills/`: List all skills for the job seeker.
  - `POST /skills/`: Add a new skill.

### 4.3. Recruiter API (`/api/v1/recruiter/`)
- **Profile:**
  - `GET /profile/`: Get the recruiter's profile.
  - `PUT /profile/`: Update the recruiter's profile.
- **Documents:**
  - `GET /documents/`: List all documents for the recruiter.
  - `POST /documents/`: Upload a new document.
  - `PUT /documents/verify/{doc_id}/`: Verify a document (admin only).

### 4.4. Job Posting API (`/api/v1/jobs/`)
- `GET /`: List all active job postings.
- `GET /{job_id}/`: Get details of a specific job posting.
- `POST /`: Create a new job posting (recruiter only).

---

## 5. Database Schema

### `users_user`
- `id`, `firstName`, `lastName`, `email`, `password`, `role`, `is_active`, etc.

### `job_seeker`
- `id`, `user_id` (FK to `users_user`), `github_url`, `linkedin_url`, `location`, `bioData`, `about`.

### `recruiter`
- `id`, `user_id` (FK to `users_user`), `companyName`, `companyLogo`, `industry`, `contactInfo`, `companyEmail`, `description`, `isVerified`.

### `job_postings`
- `id`, `recruiter_id` (FK to `recruiter`), `title`, `description`, `location`, `job_type`, `experience_level`, `is_active`.

### `skills`
- `id`, `skillName`, `description`.

### `skillSet`
- `id`, `user_id` (FK to `users_user`), `skill_id` (FK to `skills`), `proffeciency_level`.

*(... and other tables for certifications, education, etc.)*

---

## 6. Key Dependencies

- `django`: The core web framework.
- `djangorestframework`: For building RESTful APIs.
- `djangorestframework-simplejwt`: For JWT authentication.
- `celery`: For asynchronous task processing.
- `redis`: As a message broker for Celery and for caching.
- `django-channels`: For WebSocket support.
- `mysqlclient`: For connecting to MySQL.
- `python-dotenv`: For managing environment variables.
- `corsheaders`: For handling Cross-Origin Resource Sharing (CORS).
