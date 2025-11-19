people = ['sam','chris','mboya']

print(f'{people[0].title()}, could not make it.')

del people[0]

people.insert(0,'tom')
people.insert(1,'atieno')
people.append('peter')

print('I am only allowed to invite two people to the meeting')

people.pop()
people.pop()
people.pop()

print(f'{people[0]} is invited to the meeting.')
print(f'{people[1]} is invited to the meeting.')


del people[0]
del people[0]

print(people)