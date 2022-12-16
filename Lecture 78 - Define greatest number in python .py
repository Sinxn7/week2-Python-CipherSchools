def greatest(a,b,c):
    if a>b and a>c:
        return a 
    elif b>c and b>a:
        return b
    else:
        return c

a=int(input("enter first num: "))
b=int(input("enter a second num: "))
c=int(input("enter a third number: "))
print(f"{greatest(a,b,c)} is greatest")
