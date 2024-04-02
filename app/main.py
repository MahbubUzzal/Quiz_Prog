from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Answer(BaseModel):
    no: int
    body: str


class Question(BaseModel):
    no: int
    body: str
    hints: str
    reference: str
    right_answer: str
    type: str
    answers: list = [Answer]
    answer_explanation: str


class Quiz(BaseModel):
    id: int | None = None
    title: str
    prog_lang: str
    level: str
    questions: list = [Question]


@app.post("/v1/quiz", status_code=201)
async def create_quiz(quiz: Quiz):
    quiz.id = 123
    return quiz


