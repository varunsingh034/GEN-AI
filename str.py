
s = 'UPflllllllllairs soLu'
# print(s.upper()) # to capital letters
# print(s.lower()) # to lower case
# print(s.title()) # first to upper and rest lower for each word

# print(s.capitalize()) # first to upper and rest lower
print(s.casefold())
# print(s.count('l')) # no of elements

'''
 h  e  l  l  o
 0  1  2  3  4 
-5 -4 -3 -2 -1
positive -- 0 to no of char
negative -- -1 to -no of char
'''

'''
indexing -- accessing particular/single char
slicing -- accessing multiple char
'''
s = 'UPflairs soLu'

# print(s[-8])

# slicing -- [start : end : step/skip]

# print(s[2:8])
# print(s[::-1])

# print(s.find('so')) # give the index of element

# print(s.index('so')) # give the index of element

# print(s.replace('soLu',  'pvt ltd')) # replace the elements

s = '  UPflairs soLu  '


# print(s.split('l')) # break the string on to a char return a list


# print(s.strip())
# print(s.lstrip())
# print(s.rstrip())  # remove the white space from string

s = 'UPflairs soLu'
# s = ' '
# print(s.startswith('UP'))
# print(s.endswith('u')) # check the elements
# print(s.isalnum())
# print(s.isalpha())
# print(s.isdigit())
# print(s.islower())
# print(s.isupper())
# print(s.isspace())

s = 'UPflairs pvt ltd'

# print(s.center(50,'*'))
# print(s.ljust(50,'*'))
# print(s.rjust(50,'*'))
# print(s.zfill(50))
# print(s.swapcase())
# print(s.encode())
# print(s.partition(" "))
# print(s.removeprefix('UP'))
# print(s.removesuffix('ltd'))










