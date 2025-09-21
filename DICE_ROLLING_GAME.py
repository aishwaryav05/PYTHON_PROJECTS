# INSTRCUTIONS
# ASK USER TO ENTER YES OR NO
# IF USER ENTER Y : 
    # GENERATE 2 RANDOM NUMBERS AND PRINT THEM 
# IF USER ENTERS N:
    # say thank you and terminate the program 
# else
    # say invalid choice 

import random
roll_count = 0
while True:
    choice = input("Enter a choice (Y : N): ").lower()
    if choice == 'y':
        num_dice = int(input('how many dice do you want to roll: '))
        dice = [random.randint(1, 6) for _ in range(num_dice)]
        roll_count += 1
        print(f"Roll {roll_count} : {dice}")
    elif choice == 'n':
        print(f"Thank you! you have rolled {roll_count} times")
        break

    else:
        print('invalid choice!')