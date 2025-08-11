from fastapi import APIRouter
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel
from typing import List, Dict

router = APIRouter()

# --- Pydantic Models with camelCase Conversion ---
class Stream(BaseModel):
    id: str
    name: str
    description: str
    exam_count: int
    popular_exams: List[str]
    
    # This config tells Pydantic to convert snake_case to camelCase for the API
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

class ExamComparison(BaseModel):
    name: str
    difficulty: str
    duration: str
    attempts: str
    eligibility: str
    syllabus: List[str]
    career_options: List[str]
    average_salary: str
    exam_pattern: str
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)


class StreamStat(BaseModel):
    value: str
    label: str
    color: str
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

# --- Data (remains in snake_case) ---
# (Your existing streams_data, exam_details_data, and stream_stats_data go here)
# ... (I've included it below for completeness)
streams_data = [ { "id": "engineering", "name": "Engineering", "description": "Technical and engineering entrance exams including JEE, GATE, and state-level engineering exams.", "exam_count": 15, "popular_exams": ["JEE Main", "JEE Advanced", "GATE", "BITSAT"] }, { "id": "medical", "name": "Medical", "description": "Medical entrance exams for MBBS, BDS, AYUSH, and other healthcare programs.", "exam_count": 12, "popular_exams": ["NEET UG", "NEET PG", "AIIMS", "JIPMER"] }, { "id": "civil-services", "name": "Civil Services", "description": "Government job preparation including UPSC, SSC, Banking, and other competitive exams.", "exam_count": 25, "popular_exams": ["UPSC CSE", "SSC CGL", "Bank PO", "Railway"] }, { "id": "commerce", "name": "Commerce", "description": "Business and commerce related exams including CA, CS, CMA, and management entrance tests.", "exam_count": 10, "popular_exams": ["CAT", "XAT", "CA Foundation", "CS Executive"] }, { "id": "arts", "name": "Arts & Humanities", "description": "Liberal arts, literature, journalism, and humanities entrance exams.", "exam_count": 8, "popular_exams": ["CUET", "JMI", "BHU", "DU Entrance"] }, { "id": "defense", "name": "Defense Services", "description": "Military and defense services preparation including NDA, CDS, and AFCAT.", "exam_count": 6, "popular_exams": ["NDA", "CDS", "AFCAT", "Indian Navy"] } ]
exam_details_data = { "JEE Main": { "name": "JEE Main", "difficulty": "Hard", "duration": "3 hours", "attempts": "2 per year", "eligibility": "12th with PCM (75% marks)", "syllabus": ["Physics", "Chemistry", "Mathematics"], "career_options": ["Software Engineer", "Mechanical Engineer", "Civil Engineer", "Electrical Engineer"], "average_salary": "₹8-15 LPA", "exam_pattern": "MCQ + Numerical" }, "GATE": { "name": "GATE", "difficulty": "Hard", "duration": "3 hours", "attempts": "Once per year", "eligibility": "BE/BTech (Final year or passed)", "syllabus": ["Core Engineering", "Mathematics", "General Aptitude"], "career_options": ["PSU Jobs", "M.Tech", "Research", "Higher Studies"], "average_salary": "₹12-25 LPA", "exam_pattern": "MCQ + NAT" }, "BITSAT": { "name": "BITSAT", "difficulty": "Medium", "duration": "3 hours", "attempts": "Once per year", "eligibility": "12th with PCM (75% marks)", "syllabus": ["Physics", "Chemistry", "Mathematics", "English", "Logical Reasoning"], "career_options": ["Software Engineer", "Data Scientist", "Product Manager", "Research Engineer"], "average_salary": "₹10-18 LPA", "exam_pattern": "MCQ only (Computer Based)" }, "NEET UG": { "name": "NEET UG", "difficulty": "Hard", "duration": "3 hours 20 minutes", "attempts": "Once per year", "eligibility": "12th with PCB (50% marks)", "syllabus": ["Physics", "Chemistry", "Biology"], "career_options": ["Doctor", "Surgeon", "Medical Researcher", "Healthcare Professional"], "average_salary": "₹6-20 LPA", "exam_pattern": "MCQ only" }, "UPSC CSE": { "name": "UPSC CSE", "difficulty": "Hard", "duration": "Multi-stage", "attempts": "6 attempts (General)", "eligibility": "Graduate degree", "syllabus": ["General Studies", "Optional Subject", "Essay", "Ethics"], "career_options": ["IAS", "IPS", "IFS", "IRS"], "average_salary": "₹56K-2.5L per month", "exam_pattern": "Prelims + Mains + Interview" }, "CAT": { "name": "CAT", "difficulty": "Hard", "duration": "2 hours", "attempts": "Once per year", "eligibility": "Graduate degree (50% marks)", "syllabus": ["Quantitative Ability", "Verbal Ability", "Data Interpretation"], "career_options": ["Management Consultant", "Investment Banker", "Product Manager", "Business Analyst"], "average_salary": "₹15-30 LPA", "exam_pattern": "MCQ + TITA" }, }
stream_stats_data = [ {"value": "75+", "label": "Total Exams", "color": "indigo"}, {"value": "500+", "label": "Study Resources", "color": "purple"}, {"value": "50K+", "label": "Success Stories", "color": "emerald"}, {"value": "24/7", "label": "AI Support", "color": "amber"} ]


# --- Endpoints ---
# The response_model_by_alias=False is not strictly needed with populate_by_name=True, but can be good for clarity
@router.get("/streams", response_model=List[Stream], response_model_by_alias=False)
async def get_streams():
    return streams_data

@router.get("/exams", response_model=Dict[str, ExamComparison], response_model_by_alias=False)
async def get_exam_details():
    return exam_details_data

@router.get("/stream-stats", response_model=List[StreamStat], response_model_by_alias=False)
async def get_stream_stats():
    return stream_stats_data