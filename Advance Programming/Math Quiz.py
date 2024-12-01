import random

# Function to display the difficulty menu
def displayMenu():
    print("DIFFICULTY LEVEL")
    print("1. Easy")
    print("2. Moderate")
    print("3. Advanced")
    
    # Get user input for difficulty level
    while True:
        try:
            choice = int(input("Please choose a difficulty level (1-3): "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Invalid choice. Please select 1, 2, or 3.")
        except ValueError:
            print("Please enter a valid number.")

# Function to generate random integers based on difficulty level
def randomInt(difficulty):
    if difficulty == 1:  # Easy
        return random.randint(1, 9)
    elif difficulty == 2:  # Moderate
        return random.randint(10, 99)
    elif difficulty == 3:  # Advanced
        return random.randint(1000, 9999)

# Function to randomly decide whether the problem is addition or subtraction
def decideOperation():
    return random.choice(['+', '-'])

# Function to display the problem to the user and accept their answer
def displayProblem(a, b, operation):
    if operation == '+':
        print(f"{a} + {b} = ", end="")
    else:
        print(f"{a} - {b} = ", end="")
    
    # Get the user's answer
    while True:
        try:
            answer = int(input())
            return answer
        except ValueError:
            print("Please enter a valid number.")

# Function to check if the answer is correct
def isCorrect(answer, correct_answer):
    if answer == correct_answer:
        print("Correct!")
        return True
    else:
        print("Incorrect.")
        return False

# Function to display the final results and the user's rank
def displayResults(score):
    print(f"Your final score is {score} out of 100.")
    
    if score >= 90:
        print("Your rank: A+")
    elif score >= 80:
        print("Your rank: A")
    elif score >= 70:
        print("Your rank: B")
    elif score >= 60:
        print("Your rank: C")
    elif score >= 50:
        print("Your rank: D")
    else:
        print("Your rank: F")

# Function to run the quiz game
def runQuiz():
    # Display the menu and get the user's choice
    difficulty = displayMenu()
    
    # Variables to track the score and the number of questions
    score = 0
    num_questions = 10
    
    for _ in range(num_questions):
        # Generate two random numbers and a random operation
        a = randomInt(difficulty)
        b = randomInt(difficulty)
        operation = decideOperation()
        
        # Display the problem and get the user's answer
        correct_answer = a + b if operation == '+' else a - b
        user_answer = displayProblem(a, b, operation)
        
        # Check if the first answer is correct
        if isCorrect(user_answer, correct_answer):
            score += 10  # 10 points for a correct first answer
        else:
            print("You have one more chance to answer.")
            user_answer = displayProblem(a, b, operation)  # Get second attempt
            if isCorrect(user_answer, correct_answer):
                score += 5  # 5 points for a correct second answer

    # Display the results after all questions
    displayResults(score)

# Main loop to allow the user to play again
def main():
    while True:
        runQuiz()
        
        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()
