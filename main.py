from fastapi import FastAPI

app = FastAPI(title="FastAPI Demo on AWS App Runner")


@app.get("/")
async def root():
    """Root endpoint returning a welcome message."""
    return {"message": "Hello from FastAPI running on AWS App Runner!"}


@app.get("/health")
async def health_check():
    """Health check endpoint for AWS App Runner."""
    return {"status": "ok"}
