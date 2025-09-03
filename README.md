# PDF Processing with LLM Application

## Overview

This application provides a FastAPI backend for:

1. Extracting text from PDF files
2. Processing the extracted text with an LLM model

## Prerequisites

- Python 3.9+
- Docker and Docker Compose

Create a `.env` file in the project root:

```
LLM_API_KEY=your_api_key_here
```

To create docker container
```
docker-compose up -d
```

Once the application is running, you can access the API documentation at:

```
http://localhost:18000/docs
```

## API Endpoints

### PDF Processing

- **POST /pdf_processor/extract-text-ocr**
  - Upload a PDF file to extract its text content using tesseract ocr
  - Returns the extracted text
- **POST /pdf_processor/extract-text**
  - Upload a PDF file to extract its text content
  - Returns the extracted text

### LLM Processing

- **POST /llm_processor/process**
  - Extracts information from the previously extracted text according to instructions
  - Returns the LLM processing result