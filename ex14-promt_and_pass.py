#This is a code that will use a system argument and prompt the user to input some data when the script is running.
from sys import argv

#The system arguments. Remember that the order in which you declare them is very important.
filname, username = argv

prompt1 = '>>'
print(f'Hello {username}, you are running the code found in the {filname} python script.')
print(f'I will like to know if you like me?')
#Prompts the user to input in some data
like = input(prompt1)
print('why?')
reason = input(prompt1)
print(f'{username} is a cool name I like it. Please {username} do you mind telling me where you live?' )
live = input(prompt1)
print(f'''
    So if  get it all, Your name is {username}, you said {like} about liking me because {reason}
    and that you lived at {live}.
''')
