import random

while True:
    print("<< ===== ROCK PAPER SCISSORS GAME ===== >>")
    myChoice = input("Choose :: rock || paper || scissors || exit -->> quit :: \n")
    myChoice = myChoice.lower()

    if myChoice == "exit":
        break

    if myChoice != "rock" and myChoice != "paper" and myChoice != "scissors":
        print("Please choose a correct answer")
        continue

    computer_answer = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {computer_answer}")

    if myChoice == computer_answer:
        print("You tied")
    elif myChoice == "paper" and computer_answer == "rock":
        print("YOU Win!")
        break
    elif myChoice == "rock" and computer_answer == "scissors":
        print("YOU Win!")
        break
    elif myChoice == "scissors" and computer_answer == "paper":
        print("YOU Win!")
        break
    else:
        print("You lose. Try again!")
