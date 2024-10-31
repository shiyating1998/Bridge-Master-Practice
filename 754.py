import random

# Generate 4 multiplication questions
questions = [(random.randint(1000, 9999), random.randint(1000, 9999)) for _ in range(4)]

# Display questions
print("Multiplication Questions:")
for i, (a, b) in enumerate(questions, 1):
    print(f"{i}. {a} * {b}")

# Calculate and display answers
answers = [a * b for a, b in questions]
print("\nAnswers:")
for i, answer in enumerate(answers, 1):
    print(f"{i}. {answer}")
