print("=" * 50)
print("           WELCOME TO THE PYTHON QUIZ GAME")
print("=" * 50)

questions = (
    "How many elements are in the periodic table?",
    "Which animal lays the largest eggs?",
    "What is the most abundant gas in Earth's atmosphere?",
    "How many bones are in the human body?",
    "Which planet in the solar system is the hottest?"
)

options = (
    ("A. 116", "B. 117", "C. 118", "D. 119"),
    ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
    ("A. Nitrogen", "B. Oxygen", "C. Carbon Dioxide", "D. Hydrogen"),
    ("A. 206", "B. 207", "C. 208", "D. 209"),
    ("A. Mercury", "B. Venus", "C. Earth", "D. Mars")
)

answers = ("C", "D", "A", "A", "B")

guesses = []
score = 0
question_num = 0

for question in questions:
    print("\n" + "-" * 50)
    print(f"Question {question_num + 1}:")
    print(question)

    for option in options[question_num]:
        print(option)

    while True:
        guess = input("Enter your answer (A, B, C, or D): ").upper()

        if guess in ("A", "B", "C", "D"):
            break
        else:
            print("Invalid input! Please enter only A, B, C, or D.")

    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"The correct answer is {answers[question_num]}.")

    question_num += 1

print("\n" + "=" * 50)
print("                QUIZ RESULTS")
print("=" * 50)

print("Correct Answers : ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Your Answers    : ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

percentage = int((score / len(questions)) * 100)

print("\n" + "-" * 50)
print(f"Correct Answers : {score} out of {len(questions)}")
print(f"Final Score     : {percentage}%")
print("-" * 50)

if percentage == 100:
    print("Outstanding! Perfect Score!")
elif percentage >= 80:
    print("Excellent! Great Job!")
elif percentage >= 60:
    print("Good Job! Keep Learning!")
elif percentage >= 40:
    print("Fair Attempt! Practice More!")
else:
    print("Keep Practicing! You'll Improve!")

print("\nThank you for playing the Python Quiz Game!")
print("=" * 50)