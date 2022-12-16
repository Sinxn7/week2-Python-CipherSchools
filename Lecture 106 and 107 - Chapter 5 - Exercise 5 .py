def finder(list1,list2):
    list3 = []
    for i in list1:
        if i in list2:
            list3.append(i)
    return list3

print(finder([1,2,3,4] , [1,2,7,6]))
