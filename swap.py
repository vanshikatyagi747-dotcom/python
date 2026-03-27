#using third variable
a=int(input("enter a number : "))
b=int(input("enter a number : "))
print("before swap number is :", a , b) 
temp=a
a=b
b=temp
print("after swap number is : ", a , b)

#without using third variable
x=int(input("enter a number : "))
y=int(input("enter a number : "))
print("before swap number is :", x , y)
x=x+y
y=x-y
x=x-y
print("after swap number is : ", x , y)

#using xor
u=int(input("enter a number : "))
v=int(input("enter a number : "))
print("before swap number is :", u , v)
u=u^v
v=u^v
u=u^v
print("after swap number is : ", u , v)



