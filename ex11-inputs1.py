#This program is just to show how to collect data from a user into a python program

print('What is your name?', end =" ") #By default the input is taken as a string
name = input()

print ('Please, type in your address..', end =' ')
address = input()

print('Lastly, what is your profession?', end =' ')
profession = input()

print('Please tell me your age in 2019: ', end = ' ')
age = int(input()) # I used the int() to convert it into an integer to carry on mathematical operations.
year = 2019 - age
print(f'This means you were born in the year {year}')

print(f'Okay! If I got you well, your name is {name}, you are a {profession} and you leave at {address}.')