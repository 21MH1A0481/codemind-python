n=int(input())
max=0
while n>0:
    rem=n%10
    if rem>max:
        max=rem
    n=n//10
print(max)
 