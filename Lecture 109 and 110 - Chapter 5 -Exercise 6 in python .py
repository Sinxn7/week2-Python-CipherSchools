def countlist(l):
    count = 0
    for i in l:
        if type(i)== list:
            count += 1
    print(count)
    
l=['123',['sinan'],['7654'],'mankada']
countlist(l)
