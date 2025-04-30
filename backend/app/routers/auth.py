# backend/app/routers/auth.py
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel

router = APIRouter()

# Example response model for token
default_token_example = {
    "access_token": "string",
    "token_type": "bearer"
}


class Token(BaseModel):
    access_token: str
    token_type: str


@router.post("/login", response_model=Token, summary="User login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Placeholder logic: always returns a fake token
    # Replace with real authentication logic
    if form_data.username != "test" or form_data.password != "test":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
    return {"access_token": "fake-jwt-token", "token_type": "bearer"}


@router.post("/register", summary="User registration")
def register():
    # Placeholder for user registration logic
    return {"message": "User registration endpoint (not implemented)"}
