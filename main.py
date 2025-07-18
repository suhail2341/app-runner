from fastapi import FastAPI
import uvicorn

app = FastAPI(title="FastAPI Demo on AWS App Runner")


@app.get("/")
async def root():
    """Root endpoint returning a welcome message."""
    return {"message": "Hi from FastAPI running on AWS App Runner!"}


@app.get("/health")
async def health_check():
    """Health check endpoint for AWS App Runner."""
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
