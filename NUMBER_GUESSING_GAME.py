#ASK THE USER TO ENTER A NUMBER BETWEEN 1 AND 100 AND PRINT THEM 
# IF NOT A NUMBER BETWEEN 1 AND 100, SAY ENETER A VALID NUMBER
# CHOOSE THE NUMBER 
# IF THE USER NUMBER IS LESS THAN THE ACTUAL NUMBER PRINT ITS LOW
#  # IF THE USER NUMBER IS GREATER THAN THE ACTUAL NUMBER PRINT ITS HIGH
# IF THE USER NUMBER AND ACTUAL NUMBER MATCHES SAY CORRECT NUMBER 

import random 
min_val = int(input('enter a min value for range '))
max_val = int(input('enter a max value for range '))
number_to_guess = random.randint(min_val,max_val)

total_attempts = 10
best_score = 1000
attempt =0

print(f'I have seected a number between range {min_val} and {max_val}')
print(f'You have {total_attempts} attempts to guess the number')

while attempt < total_attempts:
    try:
        guess = int(input(f'Enter a number between {min_val} to {max_val}: '))
        attempt += 1
        if guess < min_val or guess > max_val :
            print(f'Please enter a number between the range {min_val} and {max_val}')
            continue

        if guess < number_to_guess:
            print('Its Too Low')
        elif guess > number_to_guess:
            print('Its too high')
        else:
            print(f"Hurray!!! you guessed the number in {attempt} attempts")
            if attempt < best_score:
                best_score = attempt
                print(f'Your best score so far is {best_score}')
            break   
    except ValueError:
        print(f'enter a valid number between {min_val} to {max_val}')

if attempt == total_attempts and guess != number_to_guess:
    print(f'sorry you have reached the maximum attempts. the correct number is {number_to_guess}')
