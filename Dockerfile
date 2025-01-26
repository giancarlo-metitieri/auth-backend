# Use the official Python 3.10 image as the base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt /app/

# Install the dependencies listed in the requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . /app/

# Install Alembic
RUN pip install alembic

# Set environment variable for Alembic configuration (optional)
ENV ALEMBIC_CONFIG=/app/alembic.ini

# Run Alembic migrations (you can modify this to suit your application)
RUN alembic upgrade head

# Expose the port FastAPI will run on
EXPOSE 8000

# Command to run FastAPI with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
