#!/usr/bin/env python3
#Author: James DuDasko

round = 0

while(True):
    round = round +1
    print( 'Finish the movie title, "Monty Python\'s The Life of _________' )
    answer = input()
    x = 'Brian'
    y = 'shrubbery'

    if(answer == x.lower() or answer == x.upper() ):
        print( 'Correct' )
        break
    elif(round == 3):
        print( 'Sorry, the answer was Brian.' )
        break
    elif(answer == y.lower() or answer == y.upper() ):
        print( 'You gave the super secret answer!' )
        break
    else:
        print( 'Sorry. Try again!' )
