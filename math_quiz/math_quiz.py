import random


def generate_random_integer(min_value, max_value):
    """
    Generate a random integer between min_value and max_value (inclusive).
    """
    return random.randint(min_value, max_value)


def generate_random_operator():
    """
    Generate a random mathematical operator from the set {+, -, *}.
    """
    return random.choice(['+', '-', '*'])


def perform_operation(num1, num2, operator):
    """
    Perform a mathematical operation based on the provided numbers and operator.
    Returns a tuple containing the problem expression and the correct answer.
    """
    expression = f"{num1} {operator} {num2}"
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    else:
        result = num1 * num2
    return expression, result

def math_quiz():
    """
    Conduct a math quiz where the user needs to answer random math problems.
    """
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)
        operator = generate_random_operator()

        problem, answer = perform_operation(num1, num2, operator)
        print(f"\nQuestion: {problem}")
        
        # Handling user input validation
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
