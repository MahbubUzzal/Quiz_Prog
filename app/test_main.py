from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

new_quiz = {
    "id": 0,
    "title": "ABC",
    "prog_lang": "python",
    "level": "level",
    "questions": [{
        "body": "body",
        "hints": "hints",
        "reference": "reference",
        "right_answer": "right_answer",
        "type": "type",
        "answers": [{
                "no": "no",
            "body": "body"
            }
        ],
        "answer_explanation": "answer_explanation",
    }],
}


def test_create_quiz():
    response = client.post("/v1/quiz", json=new_quiz)
    assert response.status_code == 201
    new_quiz["id"] = 123
    assert response.json() == new_quiz


def test_create_quiz_failed_validation():
    response = client.post("/v1/quiz", json=new_quiz)
    assert response.status_code == 406
    assert response.json() == new_quiz


