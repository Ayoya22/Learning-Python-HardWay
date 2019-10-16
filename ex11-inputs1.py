#This program is just to show how to collect data from a user into a python program

print('What is your name?', end =" ")
name = input()

print ('Please, type in your address..', end =' ')
address = input()

print('Lastly, what is your profession?', end =' ')
profession = input()

print(f'Okay! If I got you well, your name is {name}, you are a {profession} and you leave at {address}.')