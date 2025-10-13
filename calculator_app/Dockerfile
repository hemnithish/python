# Use Python 3.10 slim image
FROM python:3.10-slim-bullseye

# Update OS packages and install required tools
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends gcc libpq-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Upgrade pip once
RUN pip install --upgrade pip setuptools wheel

# Set working directory
WORKDIR /app

# Copy only requirements first (caches better)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose port (if web app)
EXPOSE 5000

# Command to run app
CMD ["python", "app.py"]
