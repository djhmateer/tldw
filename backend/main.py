# FastAPI class inherits from Starlette which is an ASGI framework for building async web services in Python
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from typing import Optional
from datetime import datetime
# import os
from pathlib import Path

# Create an instance of the FastAPI class
app = FastAPI()

# Get the project root directory (parent of backend directory)
PROJECT_ROOT = Path(__file__).parent.parent
FRONTEND_DIR = PROJECT_ROOT / "frontend"

# Mock data for demonstration - replace with database queries later
MOCK_DOCUMENTS = {
    44: {
        "id": 44,
        "title": "Sample Document",
        "content": "# Sample Document\n\nThis is a sample document with some content.\n\n## Section 1\n\nHere's some content in section 1.\n\n## Section 2\n\nAnd here's content in section 2.",
        "updated_at": "2025-01-27T10:30:00Z"
    },
    1: {
        "id": 1,
        "title": "Getting Started Guide",
        "content": "# Getting Started\n\nWelcome to TLDW! This is your first document.\n\nStart writing your content here...",
        "updated_at": "2025-01-27T09:15:00Z"
    }
}

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
@app.get("/api/items/foo")
async def get_items_foo():
    # Return a JSON response with item information
    return {"item_id": "foo", "item_name": "Foo Item", "description": "This is the foo item"}

@app.get("/api/documents/{document_id}")
async def get_document(document_id: int):
    """
    Retrieve a specific document by ID.
    
    Args:
        document_id: The ID of the document to retrieve
        
    Returns:
        Document object with id, title, content, and updated_at
    """
    if document_id not in MOCK_DOCUMENTS:
        raise HTTPException(status_code=404, detail="Document not found")
    
    return MOCK_DOCUMENTS[document_id] 