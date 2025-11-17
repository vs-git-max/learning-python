for i in range(10):
    for y in range(9):
        for z in range(8):
            print(f'({i},{y},{z})')
    
    
    
i = 1    
while i <=5:
    if i % 2==0 or i == 5:
       print('*'*2)
    else:
        print('*'*5)
    i+=1  
    
numbers = [5,2,5,2,2]

for n in numbers:
    output = ''
    for count in range(n):
        output+='x'
    print(output)         