from fastapi import FastAPI
from app.api.resume import router as resume_router

app = FastAPI()


app.include_router(resume_router, prefix="/resume", tags=["Resume"])


@app.get("/")
def root():
    return {"message": "Resume Analyzer API Running"}


@app.get("/health")
def health_check():
    return {"status": "ok"}