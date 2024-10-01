# Use the official Python image based on a slimmed-down Debian image with Python 3.10
FROM python:3.10-slim

# Set the working directory inside the container to /app
WORKDIR /app

# Copy the current directory contents (where the Dockerfile is located) to the /app directory in the container
COPY . /app

# Update the package list and install nginx and the PostgreSQL client for interacting with the PostgreSQL database
RUN apt-get update && apt-get install -y nginx postgresql-client

# Install the Python dependencies specified in the requirements.txt file, without caching to reduce image size
RUN pip install --no-cache-dir -r requirements.txt

# Copy the custom nginx configuration file from the local nginx directory to the container's nginx configuration directory
COPY nginx/nginx.conf /etc/nginx/nginx.conf

# Collect all static files for the Django app and place them in the designated static directory (usually for serving via Nginx)
RUN python manage.py collectstatic --noinput

# Expose port 80 for HTTP traffic
EXPOSE 80

# Expose port 443 for HTTPS traffic
EXPOSE 443

# Expose port 8000 for the Gunicorn application server to bind to
EXPOSE 8000

# Start the Nginx service and then run Gunicorn to serve the Django application, binding it to port 8000
CMD service nginx start && gunicorn myapp.wsgi:application --bind 0.0.0.0:8000
