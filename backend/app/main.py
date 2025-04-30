# app/main.py
from fastapi import FastAPI
# Ensure database.py initializes engine with 'sqlite+aiosqlite:///./data/aiphb.db'
# from app import models # Import models if needed for Alembic or initial setup
# from app.database import engine
from app.routers import auth, team_members  # Import your routers
from app.core.config import settings
import os  # Import os module

# Ensure data directory exists
if not os.path.exists('./data'):
    os.makedirs('./data')

# Optional: Create tables if not using Alembic initially
# models.Base.metadata.create_all(bind=engine) # Note: Use Alembic for production

# Use the application name from settings if defined, otherwise default
app_title = getattr(settings, 'PROJECT_NAME', "AI Performance Hub")
app = FastAPI(title=app_title)

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(team_members.router, prefix="/team-members", tags=["team-members"])
# ... include other routers


@app.get("/")
async def root():
    return {"message": f"{app_title} API (SQLite Alpha)"}

# Add CORS middleware if frontend is on a different origin
# from fastapi.middleware.cors import CORSMiddleware
# app.add_middleware(...)
