
chances = 0
	
while chances < 5:
	    guess = int(input('Enter your guess: '))
	
	    if guess == number:  
	        print('Congratulations! you won')
	        break
	    elif guess < number:
	        print('Your guess is low')
	    else:
	        print('Your guess is high', )
	    
	    chances = chances + 1

	    if not chances < 5:
	        print('You lose and the number is ', number)

