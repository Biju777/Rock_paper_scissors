import random
# print("Rock is designated by maintaining the fist, Scissors by extending the middle and index fingers, "
#       "and Paper by holding the hand out flat. If players throw out the same gesture, "
#       "the game goes on. If not\nit's decided by a harmonic and intransitive method — rock crushes"
#       "scissors, scissors cuts paper, but paper covers rock")
chance_for_guess = 9
count_chance = 0
computer_point = 0
human_point = 0


def display_game():
    global chance_for_guess
    global count_chance
    global computer_point
    global human_point
    # making the game in while
    while chance_for_guess > count_chance:
        print("R. For Rock, P. For paper, S. For scissors")
        user_choice = input("What do you want to choice: ")
        computer = ['R', 'P', 'S']
        bot_computer = random.choice(computer)
        # if user and computer choice same game is tie
        if user_choice.upper() == bot_computer:
            print(f"You choice {user_choice.upper()} & Computer {bot_computer} you both choice same so game is "
                  f"tie.")
        # if user choice r
        elif user_choice.upper() == 'R' and bot_computer == 'S':
            human_point = human_point + 1
            print("Rock crushes Scissors")
            print(f"You choice {user_choice.upper()} & Computer {bot_computer} so user1 Won the match.")
            print(f"\tHuman points is  {human_point}")

        # if user choice s
        elif user_choice.upper() == 'S' and bot_computer == 'P':
            human_point = human_point + 1
            print("Scissors cuts Paper")
            print(f"You choice  {user_choice.upper()} & Computer {bot_computer} so user1 Won the match.")
            print(f"\tHuman point is {human_point}")
        # if user choice p
        elif user_choice.upper() == 'P' and bot_computer == 'R':
            human_point = human_point + 1
            print("Paper cover Rock")
            print(f"You choice {user_choice.upper()} & Computer {bot_computer} so user1 Won the match.")
            print(f"\tHuman point is {human_point}")
        # if user choice s
        elif user_choice.upper() == 'S' and bot_computer == 'R':
            computer_point = computer_point + 1
            print("Rock crushes Scissors")
            print(f"You choice '{user_choice.upper()} & Computer {bot_computer} so Computer Won the match.")
            print(f"\tComputer point is {computer_point}")
        # if computer choice p
        elif user_choice.upper() == 'P' and bot_computer == 'S':
            computer_point = computer_point + 1
            print("Scissors cuts Paper")
            print(f"You choice {user_choice.upper()} & Computer {bot_computer} so Computer Won the match.")
            print(f"\tComputer point is {computer_point}")
        # if computer choice r
        elif user_choice.upper() == 'R' and bot_computer == 'P':
            computer_point = computer_point + 1
            print("Paper cover Rock")
            print(f"You choice {user_choice.upper()} & Computer {bot_computer} so Computer Won the match.")
            print(f"\tComputer point is {computer_point}")
        else:
            print("Invalid input")
            exit()
    count_chance = count_chance + 1
    print(f"You have only {chance_for_guess - count_chance} Guessed left")

    # handle the final scour who is win
    if computer_point == human_point:
        print("Both point is same so game is tia")
    elif computer_point < human_point:
        print("Human win this match.")
    else:
        print("Computer win the match!")
    print(f"Your point is {human_point} and computer point is {computer_point}")
    print('Game over!')


display_game()
