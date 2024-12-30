# Use an official Python image as the base
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy application files
COPY app.py /app/

# Install dependencies
RUN pip install flask

# Expose the port your app runs on
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
