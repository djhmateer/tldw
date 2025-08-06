# FastAPI class inherts from Starlette which is an ASGI framework for building async web services in Python
from fastapi import FastAPI

# create an instance of the FastAPI class
app = FastAPI()

# path operation decorator
# path is also called an endpoint or route

# operation refers to one of the http methods eg get, post, put, delete
@app.get("/")
# path operation function

# https://fastapi.tiangolo.com/tutorial/first-steps/#define-a-path-operation-decorator

# could be that we don't need async eg db call
# https://fastapi.tiangolo.com/async/#in-a-hurry
async def root():
    return {"message": "Hello World"}


# Define a new GET endpoint for /items/foo
@app.get("/items/foo")
async def get_items_foo():
    # Return a JSON response with item information
    return {"item_id": "foo", "item_name": "Foo Item", "description": "This is the foo item"}