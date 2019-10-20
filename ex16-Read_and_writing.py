# Reading and writing files 
from sys import argv
script, textfile = argv

print(f'''The {script} python script will erase {textfile},
            if you agree please press (Control + C)
            but if you do not agree then press "Enter"
''')
input("??")

print(f"Opening {textfile}...")

text = open(textfile, 'w')
print("Truncating(erasing it!) the file...")
text.truncate()
print("Now we will add 3 lines into it.")
line1 = input('Type in the 1st line please:')
line2 = input('Type in the 2nd line please:')
line3 = input('Type in the 3rd line please:')

print("The script will now write it back to the file")
text.write(line1)
text.write('\n')
text.write(line2)
text.write('\n')
text.write(line3)
text.write('\n')

print("Now I will close everything.")
text.close()