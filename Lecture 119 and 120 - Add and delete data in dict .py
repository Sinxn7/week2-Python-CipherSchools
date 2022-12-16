user_info={
    'name':'sinan',
    'age' : '18',
    'fav movies' : ['coco' , 'kimi na no wa'],
    'fav_tunes' : ['awakening' , 'fairy tales']
}

#add data
user_info['fav_songs']=['song1','song2']
print(user_info)
#pop method
user_info.pop('fav_tunes')
print(user_info)
more_info = {'State':'Haryana','hobbies':{'coding','reading','guitar'}}
user_info.update(more_info)
print(user_info)
