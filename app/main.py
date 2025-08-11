from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import team, streams, motivation, chat, home # Import the new routers

# Create the main FastAPI app instance
app = FastAPI()

# Add CORS Middleware
origins = ["http://localhost:5174"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the routers from other files
app.include_router(team.router, prefix="/api", tags=["Team"])
app.include_router(streams.router, prefix="/api", tags=["Streams"])
app.include_router(motivation.router, prefix="/api", tags=["Motivation"])
app.include_router(chat.router, prefix="/api", tags=["Chat"])
app.include_router(home.router, prefix="/api", tags=["Home"]) 

# A simple root endpoint to confirm the server is running
@app.get("/")
def read_root():
    return {"message": "Welcome to the SmartPrep API! Structure is now clean."}