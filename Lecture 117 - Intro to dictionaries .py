user=['sinan',24,['coco','kimi no na wa'],['awakening','fairy tale']]
#this list contains user name ,age , fav movies , fav tunes
#you can do this but it is not a good way to do this
user = {'name': 'sinan', 'age':18}
print(user)
print(type(user))
user = dict(name='zaid' , age=18)
print(user)
print(user['name'])
user_info={
    'name':'zaid',
    'age' : '18',
    'fav movies' : ['coco' , 'kimi na no wa'],
    'fav_tunes' : ['awakening' , 'fairy tales']
}
#add data in empty dictionaries
user_info2 = {}
user_info2['name'] = ['zaid']
user_info2['age'] = [18]
print(user_info2)
