from fastapi import APIRouter
from pydantic import BaseModel, ConfigDict, HttpUrl
from pydantic.alias_generators import to_camel
from typing import List

router = APIRouter()

# --- Pydantic Models with camelCase Conversion ---
class Quote(BaseModel):
    text: str
    author: str
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

class MotivationalVideo(BaseModel):
    id: str
    title: str
    speaker: str
    description: str
    duration: str
    views: str
    thumbnail: str
    embed_url: HttpUrl
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

class TimelinePhase(BaseModel):
    month: str
    activity: str
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

class SuccessStory(BaseModel):
    id: str
    name: str
    exam: str
    rank: str
    image: str
    story: str
    timeline: List[TimelinePhase]
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

# --- Data ---
quotes_data = [
    { "text": "Success is not final, failure is not fatal: it is the courage to continue that counts.", "author": "Winston Churchill" },
    { "text": "The expert in anything was once a beginner.", "author": "Helen Hayes" },
    { "text": "Don't watch the clock; do what it does. Keep going.", "author": "Sam Levenson" }
]

motivational_videos_data = [
    { "id": "1", "title": "From Failure to NEET Success - Real Journey", "speaker": "Dr. Priya Sharma", "description": "How I overcame multiple failures to finally crack NEET and become a doctor", "duration": "12:45", "views": "2.1M", "thumbnail": "/motivation-assets/priya.jpeg", "embed_url": "https://www.youtube.com/embed/dQw4w9WgXcQ" },
    { "id": "2", "title": "JEE Topper Reveals Secret Strategy", "speaker": "Rahul Gupta (AIR 47)", "description": "The mindset and daily routine that helped me crack JEE Advanced", "duration": "18:30", "views": "1.8M", "thumbnail": "/motivation-assets/rahul.jpeg", "embed_url": "https://www.youtube.com/embed/dQw4w9WgXcQ" },
    { "id": "3", "title": "UPSC Success Story - From Village to IAS", "speaker": "IAS Anita Singh", "description": "Overcoming financial struggles and social barriers to achieve the impossible", "duration": "25:15", "views": "3.5M", "thumbnail": "/motivation-assets/anita.jpeg", "embed_url": "https://www.youtube.com/embed/dQw4w9WgXcQ" },
    { "id": "4", "title": "Consistency is Key - CAT Success Mantras", "speaker": "Vikash Kumar (99.8%ile)", "description": "How daily discipline and smart work led to CAT success", "duration": "14:22", "views": "850K", "thumbnail": "/motivation-assets/vikas.jpeg", "embed_url": "https://www.youtube.com/embed/dQw4w9WgXcQ" }
]

success_stories_data = [
    { "id": "1", "name": "Anjali Patel", "exam": "NEET 2023", "rank": "AIR 156", "image": "/motivation-assets/anjali.jpeg", "story": "...", "timeline": [ { "month": "Month 1-6", "activity": "NCERT Foundation Building" }, { "month": "Month 7-14", "activity": "Intensive Practice & Mock Tests" }, { "month": "Month 15-16", "activity": "Final Revision & Strategy" } ] },
    { "id": "2", "name": "Arjun Mehta", "exam": "JEE Advanced 2023", "rank": "AIR 423", "image": "/motivation-assets/arjun.jpeg", "story": "...", "timeline": [ { "month": "Month 1-3", "activity": "Failure Analysis & Strategy Reset" }, { "month": "Month 4-10", "activity": "Focused Preparation & Practice" }, { "month": "Month 11-12", "activity": "Peak Preparation & Mock Tests" } ] }
]

# --- Endpoints ---
@router.get("/quotes", response_model=List[Quote], response_model_by_alias=False)
async def get_quotes():
    return quotes_data

@router.get("/motivational-videos", response_model=List[MotivationalVideo], response_model_by_alias=False)
async def get_motivational_videos():
    return motivational_videos_data

@router.get("/success-stories", response_model=List[SuccessStory], response_model_by_alias=False)
async def get_success_stories():
    return success_stories_data