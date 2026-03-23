num=int(input("enter a number : "))
n=num
sum=0
while(n!=0):
    rem=n % 10
    sum = sum * 10 + rem
    n = n // 10
if(sum==num):
    print("number is palindrome")
else:
    print("number is not palindrome")
