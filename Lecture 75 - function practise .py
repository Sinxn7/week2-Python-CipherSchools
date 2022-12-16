def last_character(a):
    return a[-1]
name=input()
print(last_character(name))

def even_or_odd(num):
    if num%2==0:
        print("Even")
    else:
        print("Odd")
num=int(input("Enter a number: "))
even_or_odd(num)

#Different way to define the same function

def even_or_odd(num):
    if num%2==0:
        print("Even")
    print("Odd")

num=int(input("Enter a number: "))
even_or_odd(num)

def is_even(num):
    if num%2==0:
        return True
    else:
        return False
print(is_even(10))

#Different way to define the same function

def is_even(num):
    if num%2==0:
        return True
    return False
print(is_even(10))

#Different way to define the same function

def is_even(num):
    return num%2==0
       
print(is_even(10))
