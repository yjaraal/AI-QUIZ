class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def display_question(self):
        print(self.text)
        for i, choice in enumerate(self.choices):
            print(f"{i+1}. {choice}")

    def check_answer(self, user_answer):
        return user_answer == self.answer


class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0

    def add_question(self, question):
        self.questions.append(question)

    def run_quiz(self):
        for question in self.questions:
            question.display_question()
            user_answer = input("Enter your answer (1, 2, 3, etc.): ")
            if question.check_answer(int(user_answer)):
                print("Correct!")
                self.score += 1
            else:
                print("Incorrect!")

        self.display_score()

    def display_score(self):
        print(f"\nQuiz finished!\nYour score: {self.score}/{len(self.questions)}")


# Create Quiz instance
quiz = Quiz()

# Create Question instances and add them to the quiz
question1 = Question("What is the capital of France?", ["1. Paris", "2. Rome", "3. Madrid"], 1)
quiz.add_question(question1)

question2 = Question("What is the largest planet in our solar system?", ["1. Mars", "2. Jupiter", "3. Saturn"], 2)
quiz.add_question(question2)

question3 = Question("Who painted the Mona Lisa?", ["1. Leonardo da Vinci", "2. Vincent van Gogh", "3. Pablo Picasso"], 1)
quiz.add_question(question3)

# Run the quiz
quiz.run_quiz()

