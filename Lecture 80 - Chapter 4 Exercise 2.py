def is_palindrome(string):
    if string[:] == string[::-1]:
        return True
    else:
        return False
str1=input()
print(is_palindrome(str1))

#shorter code for the same function
def is_palindrome(string):
    if string[:] == string[::-1]:
        return True
    return False
str1=input()
print(is_palindrome(str1))

#more shorter code
def is_palindrome(string):
    return(string[:] == string[::-1])
    
str1=input()
print(is_palindrome(str1))
