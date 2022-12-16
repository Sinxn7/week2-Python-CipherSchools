def input_list(l):
    e=l[0][::-1]
    g=l[1][::-1]
    o=l[2][::-1]
    print(e,g,o)
l=[['abc'],['tuv'],['xyz']]
input_list(l)

#or
def input_list(l):
    elements=[]
    for i in l:
        elements.append(i[::-1])
    return elements

words=['abc','tuv','xyz']
print(input_list(words))
