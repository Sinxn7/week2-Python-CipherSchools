def user_info(first_name,Las_name='unknown',age=24):
    print(f"Your first name is {first_name}")
    print(f"Your last name is {Las_name}")
    print(f"Your age is {age}")
user_info("Harshit","Vashisht",24)

#Lecture 84 - Variable scope in python
x=5
def func():
    global x
    x=7
    return x

print(func())
print(x)
#but
print(x) #pehle agar ye mention kia tou output 5 hoga phir function callkarne pr 7 hoga uske baad print krne pr 7 hi rahegi value
print(func())
