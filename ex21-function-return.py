def add(a,b,c):
    print(f"Adding 3 numbers {a} + {b} + {c}")
    return (a + b + c)

def div(a,b):
    print(f"Dividing {a} by {b}")
    return a/b
print("You will have to enter 3 numbers, they will all be added then the first one will be divided by the sencond and you'll se the results")
x =input("Enter the first number : ")
y =input("Enter the second number : ")
z =input("Enter the third number : ")

result1 = add(x,y,z)
result2 = div(x,y)

print(f"The result of addition is: {result1}")
print(f"The result of division is: {result2}")