print('Please think of a number between 0 and 100')

low = 0
high = 100
while True:
    guess = int((high + low) / 2)
    print('Is your secret number ' + str(guess) + '?')
    cmd = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if cmd == 'h':
        high = guess
    elif cmd == 'l':
        low = guess
    elif cmd == 'c':
        break
    else:
        print('Sorry, I did not understand your input.')
print('Game over. Your secret number was: ' + str(guess))
