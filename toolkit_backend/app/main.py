from fastapi import FastAPI
from app.routes import test

app = FastAPI()

# Include platform-specific routes
app.include_router(test.router, prefix="/api/test")
# app.include_router(twitter.router, prefix="/api/twitter")
# app.include_router(instagram.router, prefix="/api/instagram")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Automation API"}
