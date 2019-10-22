#In this program we want to copy a text form one file to another
from sys import argv
from os.path import exists

script, file_1, file_2 = argv

print(f'We will copy text from {file_1} to {file_2}')
infile_1 = open(file_1)
indata_1 = infile_1.read()

print(f'The input file is {len(indata_1)} bytes long')
print(f'Does the output file exists? {exists(file_2)}')
# opening the output folder to write into it.
outfile = open(file_2, 'w')
#writing into the output folder.
outfile.write(indata_1)

print('Everything done.')

infile_1.close()
outfile.close()