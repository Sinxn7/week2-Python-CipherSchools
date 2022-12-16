#DRY - DON'T REPEAT YOURSELF
#for i in range(start,stop,step)
for i in range(10,0,-1):
    print(i)

# Lecture 71 - FOr loop and string in python
name="sinan"
for i in name:
    print(i)

#Calculating sum of digits of a num
num=input("Enter a number: ")
total=0
for i in num:
    total += int(i)
print(total)
