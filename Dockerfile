FROM python:3.13-slim

WORKDIR /app
    
# Install system dependencies for PyMuPDF
RUN apt-get update \
    && apt-get -y install tesseract-ocr-eng \
    && apt-get install -y \
    build-essential \
    libffi-dev \
    curl \
    && rm -rf /var/lib/apt/lists/* 

RUN pip install --no-cache-dir poetry

COPY pyproject.toml ./

# Fix: Skip installing the root project
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi --no-root

# Copy application code after installing dependencies
# COPY . .

# Expose the port the app runs on
EXPOSE 18000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "18000"]