# Tuples intro
example = ('one','two','three')
days = ('monday','tuesday','wednesday')
#tuples are faster than lists
#count , index , len function , slicing can be used in tuple
for i in example:
    print(i)
#can use wile loop also
#to create a tuple with one element we must put a comma after the element
days1 , days2 , days3 = (days)
print(days1)
#list inside a tuple
favourites = ('southern mangolia',['tkoyo ghoul theme'])
favourites[1].pop()
favourites[1].append("we made it")
print(favourites)
