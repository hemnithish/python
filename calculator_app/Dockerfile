# Use Python 3.10 slim image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy your calculator_app folder into container
COPY calculator_app/ /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port (only needed if your app is web-based)
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]
