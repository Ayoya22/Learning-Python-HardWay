# This is a more compact code for the previous exercise. 
# Here we will prompte the user directly to in the input fonction
name = input('What is your name? ')
address = input('Please, type in your address.. ')
profession = input('Lastly, what is your profession? ')
age = int(input('Please tell me your age in 2019: '))
year = 2019 - age
print(f'This means you were born in the year {year}')

print(f'Okay! If I got you well, your name is {name}, you are a {profession} and you leave at {address}.')