course = 'python for beginners'
# three quotes in defining multilined  message

another = course[:]

# like 
message = '''
Hello there
Happy  to be involved in the same business
think on what can be done about this
This is out first message to you
'''

print(course[0:-1])
print(another)


name ='Jennifer'

print(name[1:-1])


# string methods
course_length = len(course)

print(course_length)

course_uppercase = course.upper()
course_lower = course.lower()

print(course_uppercase)
print(course_lower)

finding_index = course.find('p')


name_in_name= 'python 'in course

print(name_in_name)