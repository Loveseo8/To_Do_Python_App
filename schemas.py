from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str

class ProjectCreate(BaseModel):
    title: str
    user_id: int

class TaskCreate(BaseModel):
    description: str
    project_id: int
