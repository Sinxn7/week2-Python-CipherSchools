def greater(a,b):
    if a>b:
        return a
    else:
        return b
num=int(input())
num2=int(input())
bigger = greater(num,num2)
print(f"{bigger} is greater")


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
#Lecture 79

def new_greatest(a,b,c):
    bigger = greater(a,b)
    return greater(bigger,c)

print(new_greatest(10,20,30))
