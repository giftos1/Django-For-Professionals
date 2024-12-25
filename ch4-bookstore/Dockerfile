# Pull base image
FROM python:3.13.0-slim-bullseye
# Set environment variables

# Disable an automatic check for pip updates each time
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

# prevent python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# output is not buffered by Docker
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /ch4-bookstore
# Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt
# Copy project
COPY . .
