#In this program we will use python to read text files
#This code presents two methods, either through 'input()' or through 'argv'
from sys import argv

filename , textfile = argv
#We have to open the file first before trying to read it.
text = open(textfile)
print(f'This is your text file {textfile} and this is what it contains:')# We are using argv method
print(text.read()) #here we read the file and print it out.

print('Please enter your text file again..')
textfile2 = input()#Here we are using the input method.
text2 = open(textfile2)
print(text2.read())