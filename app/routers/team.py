from fastapi import APIRouter
from pydantic import BaseModel, HttpUrl, ConfigDict
from pydantic.alias_generators import to_camel
from typing import List, Optional

router = APIRouter()

# --- Pydantic Models with camelCase Conversion ---
class Socials(BaseModel):
    github: Optional[HttpUrl] = None
    linkedin: Optional[HttpUrl] = None
    email: Optional[str] = None
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

class TeamMember(BaseModel):
    name: str
    role: str
    description: str
    avatar: str
    skills: List[str]
    social: Socials
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

class Stat(BaseModel):
    number: str
    label: str
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

# --- Data ---
# (Your existing team_data and team_stats_data go here)
team_data = [ { "name": "Rakshita K Biradar", "role": "Frontend Developer", "description": "Crafting beautiful, responsive user interfaces with modern web technologies and ensuring exceptional user experiences.", "avatar": "/team-avatars/rakshita.jpg", "skills": ["React", "TypeScript", "Tailwind CSS", "UI/UX Design"], "social": { "github": "https://github.com/rakshita", "linkedin": "https://linkedin.com/in/rakshita-biradar", "email": "rakshita@smartprep.com" } }, { "name": "Anuradha", "role": "Backend Developer", "description": "Building robust, scalable server architectures and APIs that power the SmartPrep recommendation engine.", "avatar": "/team-avatars/anuradha.jpg", "skills": ["Node.js", "Python", "MongoDB", "API Development"], "social": { "github": "https://github.com/anuradhatiwari01", "linkedin": "https://linkedin.com/in/anuradha-dev", "email": "anuradha@smartprep.com" } }, { "name": "Jamal", "role": "Documentation Specialist", "description": "Creating comprehensive documentation, user guides, and ensuring clear communication across all project aspects.", "avatar": "/team-avatars/jamal.jpg", "skills": ["Technical Writing", "Documentation", "User Research", "Content Strategy"], "social": { "github": "https://github.com/jamal", "linkedin": "https://linkedin.com/in/jamal-docs", "email": "jamal@smartprep.com" } }, { "name": "Chiranjeet", "role": "ML Model Training", "description": "Developing and training machine learning models for intelligent content recommendation and personalized learning paths.", "avatar": "/team-avatars/chiranjeet.jpg", "skills": ["Machine Learning", "Python", "TensorFlow", "Data Science"], "social": { "github": "https://github.com/cheerajeev", "linkedin": "https://linkedin.com/in/cheerajeev-ml", "email": "cheerajeev@smartprep.com" } }, { "name": "Ritesh", "role": "ML Model Training", "description": "Specializing in deep learning algorithms and neural network optimization for educational content analysis and recommendation systems.", "avatar": "/team-avatars/ritesh.jpg", "skills": ["Deep Learning", "PyTorch", "NLP", "Model Optimization"], "social": { "github": "https://github.com/ritesh", "linkedin": "https://linkedin.com/in/ritesh-ai", "email": "ritesh@smartprep.com" } } ]
team_stats_data = [ { "number": "5", "label": "Team Members" }, { "number": "10+", "label": "Technologies" }, { "number": "100%", "label": "Dedication" }, { "number": "24/7", "label": "Commitment" } ]


# --- Endpoints ---
@router.get("/team", response_model=List[TeamMember], response_model_by_alias=False)
async def get_team():
    return team_data

@router.get("/team-stats", response_model=List[Stat], response_model_by_alias=False)
async def get_team_stats():
    return team_stats_data