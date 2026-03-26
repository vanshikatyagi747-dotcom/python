print("1 for addition")
print("2 for substraction")
print("3 for multiplication")
print("4 for division")
print("5 for remeinder")
print("6 for floor division")

n=int(input("enter a number  : "))

a = int(input("enter a number for calculation : "))
b = int(input("enter a number for calculation : "))

if(n == 1):
    c = a + b
    print(c)
elif(n == 2):
    c = a - b
    print(c)
elif(n == 3):
    c = a * b
    print(c)
elif(n == 4):
    if(b==0):
        print("invalid ouput")
    else:
        c = a / b
        print(c)
elif(n == 5):
    c = a % b
    print(c)
elif(n == 6):
    c = a // b
    print(c)
else:
    print("invalid input")
