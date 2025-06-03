from fastapi import FastAPI
from model import StudentRequest
from decimal import Decimal, ROUND_HALF_UP

app = FastAPI()

GRADE_SCORE = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0
}

@app.post("/score")
async def calculate_gpa(data: StudentRequest):
    total_credits = 0
    total_weighted_score = Decimal("0.0")

    for course in data.courses:
        credits = course.credits
        grade = course.grade

        score = GRADE_SCORE.get(grade, 0.0)

        total_credits += credits
        total_weighted_score += Decimal(str(credits * score))

    if total_credits == 0:
        return {"error": "No valid credits provided."}

    gpa = (total_weighted_score / total_credits).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    return {
        "student_summary": {
            "student_id": data.student_id,
            "name": data.name,
            "gpa": float(gpa),
            "total_credits": total_credits
        }
    }
