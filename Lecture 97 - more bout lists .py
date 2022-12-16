num=list(range(1,11))
print(num)
print(num.pop()) #also returns the value popped
print(num)
print(num.index(1))#list me 1 ki position dega .index()
num = [1,2,3,4,5,6,7,8,1]
print(num.index(1,3))#3rd se start krrega find krna position


def negative_list(l):
    negative = []
    for i in l:
        negative.append(-i)
    return negative
print(negative_list)
