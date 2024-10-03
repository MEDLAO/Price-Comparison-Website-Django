# Use the official lightweight Python image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the entire project into the container
COPY . /app

# Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Collect static files for serving by Nginx
RUN python manage.py collectstatic --noinput

# Expose port 8000 for Gunicorn
EXPOSE 8000

# Start Gunicorn server to serve the Django app
CMD ["gunicorn", "myapp.wsgi:application", "--bind", "0.0.0.0:8000"]
