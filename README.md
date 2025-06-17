🩻 X-Ray and Skin Disease Image Classifier

A FastAPI-based application for classifying medical images (X-Ray and Skin conditions) using deep learning.

## Features
- FastAPI backend with async support
- Modular project structure
- Support for both X-Ray and Skin disease classification
- RESTful API endpoints
- Image preprocessing and validation

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
uvicorn app.main:app --reload
```

## API Endpoints

### POST /api/diagnose
Upload a medical image for diagnosis.

**Request:**
- Content-Type: multipart/form-data
- Body: image file

**Response:**
```json
{
    "diagnosis": "string",
    "confidence": float,
    "image_type": "string"
}
```

## Project Structure
```
├── app/
│   ├── api/
│   │   └── routes.py
│   ├── core/
│   │   └── config.py
│   ├── models/
│   ├── schemas/
│   │   └── response.py
│   ├── services/
│   │   └── model_service.py
│   └── main.py
├── requirements.txt
└── README.md
```