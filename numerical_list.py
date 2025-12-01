# i think is usually done with the range method
names = ["sam", "chris", "mboya"]

for i in range(len(names)):
    print(f"{i+1}. {names[i].title()}")


# using range to make a list of names
even_numbers = list(range(2, 21, 2))

print(even_numbers)


squares = []
for i in range(0, 15, 2):
    squares.append(i**3)
print("All squares appended")
print(squares)


# cloning the lists
some_other_names = names[:]
some_other_names.append("Obange")
names.append("Peter")

print(some_other_names)
print(names)
