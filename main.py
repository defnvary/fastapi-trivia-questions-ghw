from fastapi import FastAPI
from models import TriviaResponse, Answer
import json
from typing import List

app = FastAPI()

scoreboard = {} ## username, score

## Fetch data from json

with open("questions.json") as json_file:
    questions = json.load(json_file)


# print(questions[:2])

@app.get("/trivia")
def get_trivia() -> List[TriviaResponse]:
    trivia_list = []

    for ques in questions:
        trivia = TriviaResponse (
            id = ques["id"],
            question = ques["question"],
            points = ques["points"]
        )
        # trivia = {
        #     "id": ques["id"],
        #     "question": ques["question"],
        #     "points": ques["points"]
        # }

        trivia_list.append(trivia)

    return trivia_list

## answer endpoint
@app.post("/trivia/answer/{question_id}")
def answer_question(question_id: int, answer: Answer):
    question = None

    for ques in questions:
        if ques["id"] == question_id:
            question = ques
            break

    if answer.answer.lower().strip() == question["answer"].lower().strip():
        is_correct = True
        points = question["points"]
        scoreboard[answer.username] = scoreboard.get(answer.username, 0) + points
    else:
        is_correct = False
        scoreboard.setdefault(answer.username, 0)

    return {
        "correct": is_correct,
        "score": scoreboard[answer.username]
    }