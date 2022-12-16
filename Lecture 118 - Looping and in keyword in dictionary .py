user_info={
    'name':'sinan',
    'age' : '18',
    'fav movies' : ['coco' , 'kimi na no wa'],
    'fav_tunes' : ['awakening' , 'fairy tales']
}
if 'name' in user_info:
    print("present")
else:
    print("not present")
if 'Sandarbh' in user_info.values():
    print("present")
else:
    print("not present")
for i in user_info:
        print(i)
for i in user_info.values():
        print(i)
user_info_values=user_info.values()
print(user_info.values)
