FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements_deploy.txt .
RUN pip install --no-cache-dir -r requirements_deploy.txt

# Copy application code
COPY . .

# Create directory for test uploads
RUN mkdir -p static/tests

# Expose port
EXPOSE 5000

# Set environment variables
ENV PORT=5000
ENV FLASK_DEBUG=False

# Run the application
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]