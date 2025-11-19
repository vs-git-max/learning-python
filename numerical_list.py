# i think is usually done with the range method
names = ["sam", "chris", "mboya"]

for i in range(len(names)):
    print(f"{i+1}. {names[i].title()}")


# using range to make a list of names
even_numbers = list(range(2, 21, 2))

print(even_numbers)


squares = []
for i in range(1, 15):
    j = i**2
    squares.append(j)
print("All squares appended")
print(squares)


