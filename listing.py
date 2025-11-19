names =  ['sam','chris','mboya']
print(f'My name is {names[0].title()}')
print(f'My name is {names[1].title()}')
print(f'My name is {names[-1].title()}')



names[0] = 'obange'

# names[0] = names[0].title()

# adds something at the end of the list and not at the start
names.append('samson')

# insert method adds a new item to the list at a specified place
names.insert(1,'tom')
#me thinks the index you add is the new index that the inserted value will take


del names[-2]


# pop is a funny one coz you can remove and use
popped_name = names.pop(1)
print('Popped name, ',popped_name.title())


# remove is another one it removes by value
removed_name = names.remove('chris')
print(f'Your name, {removed_name} ,was removed because your time is up.')

print(names)