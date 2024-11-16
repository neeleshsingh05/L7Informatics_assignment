# Use an official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy project files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir flask sqlalchemy

# Expose the application port
EXPOSE 4000

# Command to run the application
CMD ["python", "app.py"]

