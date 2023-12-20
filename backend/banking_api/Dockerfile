FROM ubuntu:latest
LABEL authors="adisiofialhojr"

# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app/banking_api
WORKDIR /app/banking_api

# Copy the current directory contents into the container at /app/banking_api
COPY . /app/banking_api

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn

# Set the Python path to the project directory
ENV PYTHONPATH=/app/banking_api

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV DJANGO_SETTINGS_MODULE=banking_api.api.myproject.settings

# Run gunicorn with the correct module path
CMD ["gunicorn", "banking_api.api.myproject.wsgi:application", "--bind", "0.0.0.0:8000"]

