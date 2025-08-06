# quiz.py

from questions import quiz_questions
from utils import get_valid_answer, display_score

def run_quiz():
    score = 0

    for i, q in enumerate(quiz_questions, start=1):
        print(f"\nQuestion {i}: {q['question']}")
        for option in q['options']:
            print(option)

        answer = get_valid_answer()

        if answer == q['answer']:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong. The correct answer was {q['answer']}.")

    display_score(score, len(quiz_questions))

if __name__ == "__main__":
    run_quiz()