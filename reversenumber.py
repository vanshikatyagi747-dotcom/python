n=int(input("enter a number : "))
temp=n
sum=0
while(temp!=0):
    rem=temp % 10
    sum = sum * 10 + rem
    temp = temp // 10
print(sum)
