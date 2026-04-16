# FIXED NUMBER GUESSING GAME:


special_number = 7

while True:
    n = int(input('Enter a number: '))

    if n > special_number:
        print('Bigger')
    elif n < special_number:
        print('Smaller')
    else:
        print('Congrats')
        break

    
