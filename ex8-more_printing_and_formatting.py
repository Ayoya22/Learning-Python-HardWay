formatter = '{} {} {} {}' # the variable here has 4 slots to input formatted data

print(formatter.format(2,0,1,9)) #inputs every integer into the the 4 slots 
print(formatter.format('I am ',20, 'yrs old in',2010 )) # note that the number of slots should be equal to the number of inputs.
print(formatter.format(formatter, formatter, formatter, formatter))
