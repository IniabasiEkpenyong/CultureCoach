from pydantic import BaseModel
from typing import List

class LessonRequest(BaseModel):
    name: str
    native_language: str
    target_language: str
    favorite_music: List[str]
    favorite_movies: List[str]
    hobbies: List[str]