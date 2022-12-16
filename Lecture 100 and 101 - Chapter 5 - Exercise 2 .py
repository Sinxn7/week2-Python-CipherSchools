def rev_list(l):
    print(l[::-1])


l=['1','2','3','4','5','6']
rev_list(l)
#or
def rev_list(l):
    l.reverse()
    return l


l=['1','2','3','4','5','6']
print(rev_list(l))
#using append or pop method
def rev_list(l):
    r_list=[]
    for i in range(len(l)):
        popped=l.pop()
        r_list.append(popped)
    return r_list

l=['1','2','3','4','5','6']
print(rev_list(l))
