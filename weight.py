# a project to convert weight 

weight = input('What is your weight? ')
int_weight = int(weight)

entry_standard = input('What is the standard of entry, Kilograms(K) or Pounds(L)? ')


standard_entry = entry_standard.lower()

if int_weight > 0:
    if standard_entry[0]=='k':
        user_weight = f'{int_weight/0.45}   pounds'
    elif standard_entry[0] == 'p' or standard_entry == 'l':
        user_weight= f'{int_weight*0.45} kgs'
    else:
        print('Please add the correct weight standard')
    print(f'Your weight is {user_weight}')        
else:
    print('Weight must be greater than zero')