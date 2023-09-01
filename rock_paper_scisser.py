import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    tries=6
    user_win=0
    computer_win=0
    while (tries>0):
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice not in choices:
            print("Wrong choice! Please try again.")
            continue

        computer_choice = random.choice(choices)

        print("Your choice:", user_choice)
        print("Computer choice:", computer_choice)

        if user_choice == computer_choice:
            print("It's even!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
                (user_choice == "paper" and computer_choice == "rock") or \
                (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
            user_win+=1
            
        else:
            print("Computer wins!")
            computer_win+=1
        tries-=1
    print("***********************************************************")
    print(f"number of yours win:{user_win}")
    print(f"number of computer win:{computer_win}")
    if (user_win > computer_win):
        print("So...The winner is you")
        
    elif (user_win == computer_win):
        print("So...yor and computer are even")
    else :
        print("So...The winner is the computer")


play_game()

