# Python Quiz game


questions = (
    "How many elements are there in the periodic table?:",
    "Which animal lays the Largest Eggs?:",
    "What is the most abundant gas in Earth's atmosphere?:",
    "Do you love me?:",
    "Will you Marry Me?:"
)

options = (
    ("A. 115", "B. 120", "C. 117", "D. 116"),
    ("A. Whale", "B. Dog", "C. Cat", "D. Eagle"),
    ("A. O2", "B. CO2", "C. Nitrogen", "D. None of them"),
    ("A. YES", "B. No", "C. No", "D. No"),
    ("A. No", "B. YES", "C. No", "D. No")
)

answers = ("C", "B", "D", "A", "B")
guesses = []
score = 0
question_num = 0

# Loop through the questions
for question in questions:
    print("-------------------")
    print(question)
    
    # Print the options for the current question
    for option in options[question_num]:
        print(option)

    # Get user input
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)

    # Check if the guess is correct
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("IN-CORRECT")
        print(f"{answers[question_num]} is the correct answer")  # Use current question_num here
    
    question_num += 1  # Move to the next question

print("-------------------")    
print("      RESULTS      ")    
print("-------------------")  

print("answers:" , end=(""))
for answer in answers:
    print(answer, end=(" "))
print()    


print("guesses:" , end=(""))
for guess in guesses:
    print(guess, end=(" "))
print()    


score = int(score /len(questions) * 100)
print(f"Your Score is: {score}%")
    