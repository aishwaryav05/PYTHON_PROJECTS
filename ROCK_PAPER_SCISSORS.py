# ask user to enter rock or paper or scissor 
# if not the above choice , say invalid choice 
# let the computer choose anyone 
# print user coice and computer choice with emojis
# determine the winner and print
# ask user to continue or not 

import random

ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'

emojis = {ROCK:'🪨', PAPER:'📃',SCISSORS:'✂️'}
choices = tuple(emojis.keys())

while True:
    player_score = 0
    computer_score = 0
    ties = 0

    while player_score < 2 and computer_score < 2:
        user_choice = input('Enter Rock or paper or scissor (R or p or S): ').lower()
        if user_choice not in choices:
            print('Invalid choice')
            continue
            
        computer_choice = random.choice(choices)
        print(f'You chose {emojis[user_choice]}')
        print(f'Computer chose {emojis[computer_choice]}')

        if user_choice == computer_choice:
            print('Tie!')
            ties += 1
        elif ((user_choice == ROCK and computer_choice ==SCISSORS) or
            (user_choice ==SCISSORS and computer_choice == PAPER) or
                (user_choice == PAPER and computer_choice == ROCK)):
            print('You win')
            player_score += 1
        else:
            print('Computer win! You Lose')
            computer_score += 1
        
        print(f"Score -> You: {player_score}, Computer: {computer_score}, Ties: {ties}\n")
    
    if player_score == 2:
        print('You are the overall winner\n')
    else:
        print('computer win the game\n')
    
    print(f'Total Tally -> You: {player_score}, Computer: {computer_score}, Ties: {ties}\n' )
            
    should_continue = input('Do you want to continue(Y or N): ').lower()  
    if should_continue == 'n':
        print('Bye')
        break


# REFACTORING - changing the structure of code without changing its functionality
# modularization - method of refactoring , its the process of breaking the code into smaller reusuable code called modules or functions 