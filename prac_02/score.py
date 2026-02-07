"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random


def main():
    """Ask the user for their score and print the result, then show random score result."""
    score = float(input("Enter score: "))
    result = determine_result(score)
    print(f"User score {score} is {result}")

    if result == "Excellent":
        print("You get a prize!")

    random_score = random.uniform(0, 100)
    random_result = determine_result(random_score)
    print(f"Random: {random_score:.0f} = {random_result}")


def determine_result(score):
    """Return the result for a given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()