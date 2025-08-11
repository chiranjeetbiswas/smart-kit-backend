from fastapi import APIRouter
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel
from typing import List

router = APIRouter()

# --- Pydantic Model for Testimonials ---
class Testimonial(BaseModel):
    name: str
    exam: str
    quote: str
    rating: int
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

# --- Data ---
testimonials_data = [
    { "name": "Priya Sharma", "exam": "NEET 2024 Qualifier", "quote": "SmartPrep's AI recommendations helped me focus on the right resources. Cleared NEET in my first attempt!", "rating": 5 },
    { "name": "Rahul Gupta", "exam": "JEE Advanced 2024", "quote": "The personalized roadmap and book recommendations saved me months of preparation time.", "rating": 5 },
    { "name": "Anjali Patel", "exam": "UPSC CSE 2023", "quote": "SmartPrep's curated content and motivation section kept me on track throughout my UPSC journey.", "rating": 5 }
]

# --- Endpoint ---
@router.get("/testimonials", response_model=List[Testimonial], response_model_by_alias=False)
async def get_testimonials():
    return testimonials_data