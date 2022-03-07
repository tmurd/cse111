# Place holder for postive(p) and negative(n) questions
p = 0
n = 0


def main():
    # Explanation of the test
    print(f"\nThis program is an implementation of the Rosenberg")
    print(f"Self-Esteem Scale. This program will show you ten")
    print(f"statements that you could possibly apply to yourself.")
    print(f"Please rate how much you agree with each of the")
    print(f"statements by responding with one of these four letters:")
    print(f"\nD means you strongly disagree with the statement.\nd means you disagree with the statement.\na means you agree with the statement.\nA means you strongly agree with the statement.\n")

    # Use as starting number for the score
    score = 0

    # Questions to ask and run through the compute_score function and continously summed
    score += compute_score("\n1. I feel that I am a person of worth, at least on an equal plane with others.", "p")
    score += compute_score("\n2. I feel that I have a number of good qualities.", "p")
    score += compute_score("\n3. All in all, I am inclined to feel that I am a failure.", "n")
    score += compute_score("\n4. I am able to do things as well as most other people.", "p")
    score += compute_score("\n5. I feel I do not have much to be proud of.", "n")
    score += compute_score("\n6. I take a positive attitude toward myself.", "p")
    score += compute_score("\n7. On the whole, I am satisfied with myself.", "p")
    score += compute_score("\n8. I wish I could have more respect for myself.", "n")
    score += compute_score("\n9. I certainly feel useless at times.", "n")
    score += compute_score("\n10. At times I think I am no good at all.", "n")

    # Final analysis shown to user
    print(f"\nYour score is {score}\nA score below 15 may indicate problematic low self-esteem.")
    print()

# Function used to compute each user answer based on answer degree and positive(p) or negative(n) question
def compute_score(question, p_or_n):
    # Uses question from main function
    print(question)
    # Obtain answer from user
    answer = input("Enter D, d, a, or A: ")
    # Place-holder for score for the specific answer
    score = 0
    # Give score according to user answer
    if answer == "D":
        score = 0
    elif answer == "d":
        score = 1
    elif answer == "a":
        score = 2
    elif answer == "A":
        score = 3
    # Adjust score if question was negative(n)
    if p_or_n == "n":
        score = 3 - score
    # Return score value for the answer to the specifc question
    return score

# Run the main function to display to user
main()