def greater(a,b):
    if a>b:
        return a
    else:
        return b
num=int(input())
num2=int(input())
bigger = greater(num,num2)
print(f"{bigger} is greater")
