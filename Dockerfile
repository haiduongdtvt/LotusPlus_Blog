FROM python:3.12-slim

#Set enviroment variable
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_APP=run.py
ENV FLASK_ENV=production
ENV DATABASE_URL="sqlite:///app.db"
#Create and set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/list/*

# Install Python dependencies
COPY requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY ..

# Create uploads directory
RUN mkdir -p /app/app/uploads && \
    chmod -R 777 /app/app/uploads \

# Run application
CMD ["gunicorn", '--bind', '0.0.0.0:5000', "run:run"]