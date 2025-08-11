import os
import google.generativeai as genai
from fastapi import APIRouter
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel
from typing import List, Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

router = APIRouter()

# --- Gemini API Configuration ---
try:
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    if not gemini_api_key:
        raise ValueError("GEMINI_API_KEY not found in environment variables.")
    genai.configure(api_key=gemini_api_key)
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
except Exception as e:
    print(f"Error during Gemini configuration: {e}")
    model = None


# --- Master Prompt for the AI Mentor (UPDATED FOR MULTIPLE EXAMS) ---
MASTER_PROMPT = """
You are an elite-level AI mentor for competitive exam preparation in India. Your expertise covers three main domains: Engineering (JEE Main & Advanced), Medical (NEET), and Civil Services (UPSC CSE).

Your knowledge is based on:
- For UPSC: Standard books (Laxmikanth, NCERTs, Spectrum), government sources (PIB, PRS), and previous year questions.
- For Engineering (JEE): Standard books (H.C. Verma, R.D. Sharma, I.E. Irodov), NCERT Physics, Chemistry, and Math.
- For Medical (NEET): Standard books (NCERT Biology, Chemistry, Physics), and popular coaching materials.
- Logical thinking, scientific principles, and problem-solving strategies for each exam.

You must:
1.  First, identify which exam domain (UPSC, JEE, or NEET) the user's question relates to.
2.  Provide structured, accurate, and syllabus-aligned answers for that specific exam.
3.  Break down difficult concepts into simple, understandable ideas.
4.  Handle factual, conceptual, analytical, and strategy-based questions.
5.  Maintain a formal, precise, and encouraging tone.
6.  Provide structured booklists or resource recommendations when asked.

NEVER:
- Confuse the syllabus or strategy of one exam with another.
- Generate politically biased, fake, or sensational content.
- Answer personal or irrelevant queries.
- Use casual or informal language.

Treat all questions as if asked by a serious aspirant preparing for their respective competitive exams.
"""

# --- Pydantic Models for our API ---
class ChatRequest(BaseModel):
    message: str # Our frontend sends a 'message' key

class Recommendation(BaseModel):
    # This is here to match the frontend, but Gemini won't generate it for now
    id: int
    title: str
    description: str
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

class ChatResponse(BaseModel):
    text: str # Our frontend expects a 'text' key
    recommendations: Optional[List[Recommendation]] = None
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)


# --- POST Endpoint for Chat Logic ---
@router.post("/chat", response_model=ChatResponse)
async def handle_chat_message(request: ChatRequest):
    if not model:
        return ChatResponse(text="Sorry, the AI model is not available right now. Please check the server configuration.")

    try:
        user_question = request.message
        if not user_question:
            return ChatResponse(text="Please provide a question.")

        full_prompt = f"{MASTER_PROMPT}\n\nUser Question: \"{user_question}\"\n\nMentor's Answer:"
        
        # Generate response from Gemini
        response = model.generate_content(full_prompt)
        bot_answer = response.text

        # Return the response in the format our frontend expects
        return ChatResponse(text=bot_answer, recommendations=[])

    except Exception as e:
        print(f"An error occurred: {e}")
        return ChatResponse(text="Sorry, an error occurred while processing your request.")