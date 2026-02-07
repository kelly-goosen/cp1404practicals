"""
CP1404/CP5632 - Practical
Program to determine score status
"""

def main():
    """Ask the user for their score and print the result."""
    score = float(input("Enter score: "))
    result = determine_result(score)


def determine_result(score):
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")

main()