from fastapi import FastAPI
from app.features.auth.routes import router as auth_router

app = FastAPI(title="CampusFlow CRM")

# Include auth routes under /auth prefix
app.include_router(auth_router, prefix="/auth", tags=["auth"])

@app.get("/")
async def root():
    return {"message": "Welcome to CampusFlow CRM API"}
