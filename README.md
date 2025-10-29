# DealSync - Wagtail CMS Project

This is a Wagtail-based CMS project built on Django with SQLite database.

## Project Structure

- `dealsync/` - Main Django settings and WSGI config
- `home/` - Homepage models, templates, and static CSS
- `search/` - Search functionality implementation
- Uses SQLite as the database
- Dockerized application with Nginx reverse proxy

## CI/CD Pipelines

This project includes several GitHub Actions workflows for continuous integration and deployment:

### 1. CI/CD Pipeline (`ci-cd.yml`)
- Runs tests on every push and pull request
- Builds Docker image
- Deploys to production on pushes to main branch

### 2. Code Quality and Security (`code-quality.yml`)
- Runs Python linting with flake8
- Performs security scanning with Bandit
- Uploads security reports

### 3. Docker Image Building (`docker.yml`)
- Builds and publishes Docker images
- Tags images appropriately (branch, PR, version tags)
- Pushes to DockerHub on pushes to main branch

### 4. Manual Deployment (`deploy.yml`)
- Manual deployment trigger
- Can be run on demand for production deployment

## Setting up CI/CD

To use these workflows, you need to set up the following secrets in your GitHub repository:

1. `DOCKER_USERNAME` or `DOCKERHUB_USERNAME` - Your DockerHub username
2. `DOCKER_PASSWORD` or `DOCKERHUB_TOKEN` - Your DockerHub access token

## Local Development

To run the project locally with Docker:

```bash
docker-compose up
```

The application will be available at http://localhost

## Production Deployment

For production deployment, update the deploy job in the workflows with your specific deployment commands.

## Database

This project uses SQLite as the database. The database file (`db.sqlite3`) is mounted as a volume in the Docker setup to persist data between container restarts.