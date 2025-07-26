from app.schemas import LessonRequest

def generate_fake_lesson(request: LessonRequest):
    return {
        "lesson_title": f"Intro to {request.target_language} for {request.name}",
        "vocabulary": ["hola", "gracias", "cultura"],
        "dialogue": "A: Hola, ¿te gusta Bad Bunny? B: ¡Sí, me encanta!",
        "cultural_tip": f"In {request.target_language}-speaking countries, music often reflects deep regional identity.",
    }