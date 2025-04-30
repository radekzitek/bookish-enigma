from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()


# Example Pydantic model for a team member
class TeamMember(BaseModel):
    id: int
    name: str
    role: str


# In-memory fake database for demonstration
fake_team_members = [
    TeamMember(id=1, name="Alice", role="Developer"),
    TeamMember(id=2, name="Bob", role="Designer"),
]


@router.get("/", response_model=List[TeamMember], summary="List all team members")
def list_team_members():
    return fake_team_members


@router.get(
    "/{member_id}", response_model=TeamMember, summary="Get a team member by ID"
)
def get_team_member(member_id: int):
    for member in fake_team_members:
        if member.id == member_id:
            return member
    raise HTTPException(status_code=404, detail="Team member not found")
