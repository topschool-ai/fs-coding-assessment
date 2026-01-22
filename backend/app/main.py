"""Main FastAPI application module."""

from fastapi import FastAPI

# Create FastAPI instance
app = FastAPI(
    title="Todo API",
    description="Todo management API with authentication",
    version="1.0.0",
    # lifespan=lifespan,  # TODO: Uncomment when lifespan is implemented
)


@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "Todo API is running!", "version": "1.0.0", "docs": "/docs"}
