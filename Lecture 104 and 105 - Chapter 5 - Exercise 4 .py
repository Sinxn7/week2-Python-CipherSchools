def filteroddeven(l):
    oddnums = []
    evennums= []
    for i in l:
        if i % 2 == 0:
            evennums.append(i)
        else:
            oddnums.append(i)
    output = [oddnums , evennums]
    return output

nums=[1,2,3,4,5,6,7,8,9]
print(filteroddeven(nums))
