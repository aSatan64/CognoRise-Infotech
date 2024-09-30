import random
print("====================================================================")
print("=================== Rock, Paper, Scissors Game =====================")
print("====================================================================")

first = 0
score = 0
while 1:
    def main_game():
        choices = ["rock", "paper", "scissors"]
        user_choice = input("Choose (Rock, Paper, Scissors): ").lower()
        randchoice = random.choice(choices)
        def user_rock():
            global score
            if randchoice == "rock":
                print("Tie!")
            elif randchoice == "paper":
                print("Paper covers rock. You lose!")
                score =score - 1
            elif randchoice == "scissors":
                print("Rock smashes scissors. You win!")
                score = score + 1

        def user_paper():
            global score
            if randchoice == "rock":
                print("Rock crushes paper. You win!")
                score =score + 1
            elif randchoice == "paper":
                print("Paper covers paper. It's a tie!")
            elif randchoice == "scissors":
                print("Scissors cuts paper. You lose!")
                score = score - 1

        def user_scissors():
            global score
            if randchoice == "rock":
                print("Rock smashes scissors. You lose!")
                score = score - 1
            elif randchoice == "paper":
                print("Scissors cuts paper. You win!")
                score = score + 1
            elif randchoice == "scissors":
                print("Scissors cuts scissors. It's a tie!")

        print("====================================================================")
        if user_choice == "rock":
            print("Computer chose "+ randchoice+"!")
            user_rock()
        elif user_choice == "paper":
            print("Computer chose "+ randchoice+"!")
            user_paper()
        elif user_choice == "scissors":
            print("Computer chose "+ randchoice+"!")
            user_scissors()
        else:
            print("Invalid choice. Please choose (Rock, Paper, Scissors).")
        print("Your current score is: ", score)
        print("====================================================================")
    while first==0:
        main_game()
        first=1
    play_again = input("Do you want to play again? (yes/no): ")
    print("====================================================================")
    
    if play_again.lower() == "yes":
            main_game()
    else:
        print("Your final score is: ", score)
        break