from fastapi import FastAPI
from app.schemas import LessonRequest
from app.lesson_generator import generate_fake_lesson

app = FastAPI(title="CultureCoach API")

@app.post("/generate-lesson")
def generate_lesson(request: LessonRequest):
    lesson = generate_fake_lesson(request)
    return lesson