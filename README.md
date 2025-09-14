## Task manager

### Hexlet tests and linter status:
[![Actions Status](https://github.com/sergeikuz/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/sergeikuz/python-project-52/actions)
[![Actions Status](https://github.com/sergeikuz/python-project-52/actions/workflows/ci.yml/badge.svg)](https://github.com/sergeikuz/python-project-52/actions)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=sergeikuz_python-project-52&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=sergeikuz_python-project-52)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=sergeikuz_python-project-52&metric=coverage)](https://sonarcloud.io/summary/new_code?id=sergeikuz_python-project-52)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=sergeikuz_python-project-52&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=sergeikuz_python-project-52)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=sergeikuz_python-project-52&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=sergeikuz_python-project-52)

[Please visit my Task manager on render.com](https://python-project-52-i3tm.onrender.com)

### Description
A Django-based task management system that allows users to create, track, and manage tasks with statuses and labels.

This is project ["Task manager"](https://ru.hexlet.io/programs/python/projects/52) on the Python Development course on [Hexlet.io](https://ru.hexlet.io/programs/python)

### Features
User authentication and authorization
Task management (create, read, update, delete)
Status management for tasks
Label management for task categorization
Internationalization support (i18n)
Responsive design

### Project Structure
task_manager/ - Main application directory
users/ - User management
tasks/ - Task management
statuses/ - Task status management
labels/ - Task label management
templates/ - HTML templates
locale/ - Translation files

### Setup and Installation
Clone the repository
```
git clone git@github.com:sergeikuz/python-project-52.git
```
### Install dependencies:
```
make install
```
### Start the application:
```
make run
```
### Development
#### Run tests:
```
make test
```
### Check code style:
```
make lint
```
### Environment Variables
#### The application requires the following environment variables:
```
# Django settings
SECRET_KEY=yoursecretkeyhere
DEBUG=True  # Set to False in production
ALLOWED_HOSTS=localhost,127.0.0.1,yourdomain.com

# Rollbar settings (optional)
ROLLBAR_ACCESS_TOKEN=youraccesstokenhere

# Database settings (for PostgreSQL)
DATABASE_URL=postgres://user:password@localhost:5432/dbname
```
### Technology Stack
#### Backend
- Python 3.10+: Modern Python version with enhanced features
- Django 5.2: Latest stable Django framework for robust web development
- Django ORM: Sophisticated object-relational mapping for database interactions
- PostgreSQL: Production-grade relational database for data reliability
- SQLite: Lightweight database for development and testing

#### Frontend
- HTML5: Modern markup language for web content
- Bootstrap 5: Responsive design framework with modern UI components
- Django Templates: Server-side rendering with Django's template engine

### Security
- Authentication System: Django's built-in authentication system with custom user model
- Permission Checks: Custom mixins ensuring proper access control
- CSRF Protection: Cross-Site Request Forgery protection
- Environment Variables: Secure configuration using environment variables
- Password Hashing: Secure password storage with Django's authentication system

### Testing
- Django Test Framework: Comprehensive testing tools for Django applications
- Pytest: Advanced testing framework for Python
- Coverage Reports: Test coverage analysis to ensure code quality

### CI/CD
- GitHub Actions: Automated testing, linting, and deployment workflows
- SonarQube Integration: Code quality and security analysis

### Monitoring & Error Tracking
- Rollbar: Real-time error tracking and monitoring

### Development Tools
- Makefile: Project automation for common tasks
- UV: Modern dependency management for Python
- Flake8: Code linting to maintain code quality
- Whitenoise: Static file serving for production
- Gunicorn: Production-ready WSGI server

### Good luck and have a fun!) 🤚