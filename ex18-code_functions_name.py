#I will write 4 functions that will certain things this is so just for us to understand how they all work.
def print_2(*args):
    args1, args2 = args
    print(f'args1:{args1}, args2:{args2}')

#second function
def print_2_again(args1, args2):
    print(f'args1:{args1}, args2:{args2}')

#Third function
def print_1(args1):
    print(f'args1:{args1}')

#fourth...
def print_none():
    print("I got nothing, can't print something")

print_2("Yaounde", "Douala")
print_2_again("Yaounde", "Douala")
print_1("Yaounde")
print_none()