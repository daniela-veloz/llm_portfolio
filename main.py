from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """
    Root endpoint that returns a simple greeting message.
    
    Returns:
        dict: A dictionary containing a "Hello World" message
    """
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    """
    Personalized greeting endpoint.
    
    Args:
        name (str): The name to include in the greeting message
        
    Returns:
        dict: A dictionary containing a personalized greeting message
    """
    return {"message": f"Hello {name}"}
