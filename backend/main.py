# FastAPI class inherits from Starlette which is an ASGI framework for building async web services in Python
from fastapi import FastAPI
from fastapi.responses import FileResponse
import os
from pathlib import Path

# Create an instance of the FastAPI class
app = FastAPI()

# Get the project root directory (parent of backend directory)
PROJECT_ROOT = Path(__file__).parent.parent
FRONTEND_DIR = PROJECT_ROOT / "frontend"

# Path operation decorator
# Path is also called an endpoint or route

# Operation refers to one of the http methods eg get, post, put, delete
@app.get("/")
# Path operation function
async def root():
    """Serve the main index.html file"""
    index_path = FRONTEND_DIR / "index.html"
    return FileResponse(str(index_path))

@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "message": "TLDW is running"}

# Define a new GET endpoint for /items/foo
@app.get("/items/foo")
async def get_items_foo():
    # Return a JSON response with item information
    return {"item_id": "foo", "item_name": "Foo Item", "description": "This is the foo item"} 