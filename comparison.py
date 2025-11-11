temperature  = 30


if temperature > 30:
    print('Its a hot day')
else:
    print('Its not a hot day')    
    
    
    
#some work here
# taking an input and then checking if the name has more than 3 characters and less than 50
name = input('What is your name? ')

name_length = len(name)
print(name_length)

if name_length <3:
    print('Name must be at least three characters long')
elif name_length <= 50:
    print('What a wonderful name')
else:
    print('Your name is too long')