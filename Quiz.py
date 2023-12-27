class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question):
        print(question["Question"])
        for i, option in enumerate(question["options"], start=1):
            print(f"{i}. {option}")

        while True:
            user_answer = input(" Enter Your choice (Enter the number): ")
            if user_answer.isdigit():
                user_choice = int(user_answer)
                if 1 <= user_choice <= len(question["options"]):
                    return user_choice
                else:
                    print("Invalid input! Please enter a valid number.")
            else:
                print("Invalid input! Please enter a valid number.")

    def evaluate_answer(self, user_choice, correct_answer, question_number):
        if user_choice == correct_answer:
            print(f"Question {question_number}: Correct! You earned 1 point.\n")
            self.score += 1
        else:
            print(f"Question {question_number}: Wrong! The correct answer was {correct_answer}: {self.questions[question_number-1]['options'][correct_answer-1]}\n")

    def run_quiz(self):
        for i, question in enumerate(self.questions, start=1):
            user_choice = self.display_question(question)
            self.evaluate_answer(user_choice, question["answer"], i)

        print(f"Quiz complete! Your final score: {self.score}/{len(self.questions)}")

        #question are


def main():
    custom_questions = [
        {
            "Question": "What is the capital of India?",
            "options": ["Mumbai", "Delhi", "Gujrat", "Karnataka"],
            "answer": 2,
        },
        {
            "Question": "Which programming language is known for its readability?",
            "options": ["Java", "Python", "C++", "JavaScript"],
            "answer": 2,
        },
        {
            "Question": "Which is the no1 city in India?",
            "options": ["Pune", "Nagpur", "Nashik", "Mumbai"],
            "answer": 4,
        },
    ]

    
    quiz = Quiz(custom_questions)
    quiz.run_quiz()


if __name__ == "__main__":
    main()
