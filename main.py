from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import questions

app = FastAPI(
    title="TDS Virtual Tutor API",
    description="API for TDS Virtual Tutor application",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure this for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(questions.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "TDS Virtual Tutor API is running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 