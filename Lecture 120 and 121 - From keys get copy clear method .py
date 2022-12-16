#fromkeys
# d = {'name}: 'unknown' , 'age' : 'unknown'}
d = dict.fromkeys(['name','age','height'],'unknown')
print(d)
#but if u write "abc" it will be a key bkey and c key
d = dict.fromkeys("abc",'unknown')
print(d)
#using range
d = dict.fromkeys(range(1,11),'unknown')
print(d)

#get method
d = {'name':"unknown", 'age' : 'unknown'}
print(d['name'])
print(d.get('name'))
print(d.get('names'))
#output will be none in get method
d.clear()
print(d)
