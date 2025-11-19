names = ['Sam', 'Chris', 'Mboya', 'Phone', 'Rose']

print(names[:])


numbers = [1,2,3,4,56,7,8,9,10]

max = numbers[0]
print(max)
for number in numbers:
    if number > max:
        max = number
print(max)        


# 2d list
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]

matrix[1][1] = 20

print(matrix[1][1])


for row in matrix:
    for i in row:
        print(i)
        
        
numbers.append(13)
print(numbers) 

numbers.insert(0,[13,23,45,0])       

print(numbers)

numbers.remove(56)

print(numbers)

numbers.pop()

print(numbers)

index = numbers.index(3)
print(index)

numbers.clear()

print(numbers)



