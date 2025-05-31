# TDS Virtual Tutor API

A FastAPI-based REST API for the TDS Virtual Tutor application.

## Project Structure

```
├── main.py                 # FastAPI application entry point
├── requirements.txt        # Python dependencies
├── app/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── question.py     # Pydantic models for questions
│   └── routers/
│       ├── __init__.py
│       └── questions.py    # Question-related endpoints
└── README.md
```

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the development server:**
   ```bash
   python main.py
   ```
   
   Or using uvicorn directly:
   ```bash
   uvicorn main:app --reload
   ```

## API Endpoints

The API will be available at `http://localhost:8000`

### Available Endpoints

- `GET /` - Root endpoint
- `GET /health` - Health check
- `POST /api/v1/questions` - Create a new question (dummy implementation)
- `GET /api/v1/questions` - Get all questions (dummy implementation)
- `GET /api/v1/questions/{question_id}` - Get specific question (dummy implementation)

### API Documentation

Once the server is running, you can access:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Development

The question endpoints at `/api/v1/questions` are currently dummy implementations. Replace the logic in `app/routers/questions.py` with your actual business logic.

### Question Model

The question model includes:
- `title`: Question title
- `content`: Question content/description
- `difficulty`: Question difficulty level (optional, defaults to "medium")
- `category`: Question category (optional)
- `tags`: List of tags (optional)

## Next Steps

1. Add database configuration (SQLAlchemy/MongoDB)
2. Implement actual question CRUD operations
3. Add authentication and authorization
4. Add input validation and error handling
5. Add logging and monitoring
6. Configure environment variables 