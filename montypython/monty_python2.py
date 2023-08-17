#!/usr/bin/env python3


#creating a loop that must be broken manually in the following code
round = 0
while True:
    round = round + 1
    print('Finish the movie title, "Monty Python\'s The Life of ______"')
    answer = input("Your guess--> ")
    #breaks the loop if q is answered correctly
    if answer == 'Brian':
        print('Correct')
        break
    #breaks the loop if too many incorrect guesses
    elif round==3:
        print("Sorry, the answer was Brian.")
        break
    else:
        print("Sorry! Try again!")
