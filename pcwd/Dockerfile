# Use the official Python image
FROM python:3.10

# Install system packages required to compile psycopg2 (PostgreSQL adapter for Python) and AWS CLI
RUN apt-get update && apt-get install -y build-essential libpq-dev gcc curl unzip

# Install AWS CLI inside the Docker container
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && unzip awscliv2.zip && ./aws/install && rm -rf awscliv2.zip aws

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1 # Prevent Python from generating .pyc files
ENV PYTHONUNBUFFERED 1 # Force Python to output logs to stdout/stderr immediately without buffering
ENV DJANGO_ENV production

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Verify Gunicorn is installed
RUN gunicorn --version

# Copy the entire project to the container
COPY . /app/

# Make the entrypoint script executable
RUN chmod +x /app/docker-entrypoint.sh

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port 8000
EXPOSE 8000

# Start the Gunicorn server
CMD ["/bin/sh", "-c", "/app/docker-entrypoint.sh && gunicorn pcwd.wsgi:application --bind 0.0.0.0:8000"]
