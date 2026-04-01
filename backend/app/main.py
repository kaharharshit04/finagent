from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

from app.routes import upload, query

app = FastAPI(title="FinAgent API")

# CORS (VERY IMPORTANT for frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(upload.router)   
app.include_router(query.router)


@app.get("/")
def root():
    return {"message": "FinAgent Backend Running 🚀"}