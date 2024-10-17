# Use the official lightweight Python image
FROM python:3.10-slim

# Install system packages required to compile psycopg2 (PostgreSQL adapter for Python)
RUN apt-get update && apt-get install -y build-essential libpq-dev gcc

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

# Copy the entire project to the container
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port 8000
EXPOSE 8000

# Start the Gunicorn server
CMD ["gunicorn", "pcwd.wsgi:application", "--bind", "0.0.0.0:8000"]
