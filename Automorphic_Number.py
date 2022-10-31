n=int(input())
m=n**2
l=len(str(n))
num=m%(10**l)
if n==num:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")