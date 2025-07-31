def show_score(score, total):
    """
    Displays the user's final score.

    Parameters:
    - score (int): The number of correct answers.
    - total (int): The total number of questions.
    """
    print("\n--- Quiz Completed ---")
    print(f"Your score is {score} out of {total}.")
    print(f"Percentage: {score / total * 100:.2f}%")