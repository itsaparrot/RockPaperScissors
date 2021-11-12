import random


def win_decider(computer_choice, player_choice):
    # returns 1 (player win) 2 (computer win) 3 (DRAW)
    if user_choice == 'rock':
        if npc_selection == 'rock':
            decider = 3
        elif npc_selection == 'paper':
            decider = 2
        else:
            decider = 1
    if user_choice == 'paper':
        if npc_selection == 'paper':
            decider = 3
        elif npc_selection == 'scissors':
            decider = 2
        else:
            decider = 1
    if user_choice == 'scissors':
        if npc_selection == 'scissors':
            decider = 3
        elif npc_selection == 'rock':
            decider = 2
        else:
            decider = 1
    return decider


# creates list of valid choices, then has computer pick one
choices = ['rock', 'paper', 'scissors']
npc_selection = random.choice(choices)

game_continue = True
while game_continue:
    user_choice = input('Rock, Paper, or, Scissors?').lower()
    # checks if user made a valid selection
    if user_choice in choices:
        print(f"Computer chose: {npc_selection}!")
        # runs win decider with user's selection and computers selection
        outcome = win_decider(npc_selection, user_choice)
        if outcome == 1:
            print("You win!")
        elif outcome == 2:
            print("You lost, try again!")
        else:
            print("Draw!")
        # checks if user wants to play again, runs until a valid answer is given
        valid_continue = True
        while valid_continue:
            check_continue = input("Would you like to play again? 'yes' or 'no': ").lower()
            if check_continue == 'yes':
                valid_continue = False
            elif check_continue == 'no':
                valid_continue = False
                game_continue = False
    else:
        print('Not a valid selection.')
