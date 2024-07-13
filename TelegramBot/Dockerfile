# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set environment variables to prevent Python from writing pyc files to disc
# and to ensure the stdout and stderr streams are immediately flushed.
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Ensure the .env file is copied to the container
COPY .env /app/.env

# Copy the responses.json file to the working directory
COPY responses.json /app/responses.json

# Set the command to run the bot
CMD ["python", "telegram_bot.py"]
