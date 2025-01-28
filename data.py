import requests
import html

parameters = {
    "amount": 10,
    "type": "boolean"
}

try:
    response = requests.get("https://opentdb.com/api.php", params=parameters)
    response.raise_for_status()
    data = response.json()
    question_data = data["results"]

    # Sanitize questions
    for question in question_data:
        question["question"] = html.unescape(question["question"])
        question["correct_answer"] = html.unescape(question["correct_answer"])
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
    # Fallback to a static list of questions in case of API failure
    question_data = [
        {
            "category": "Science: Computers",
            "type": "boolean",
            "difficulty": "easy",
            "question": "Linus Torvalds created Linux and Git.",
            "correct_answer": "True",
            "incorrect_answers": ["False"]
        },
        # Add other static questions here...
    ]
