# working on the logic of the program using loops
number_of_trial =1
while number_of_trial <=3:
    number_of_trial+=1    
    int_weight = int(input('What is your weight? '))
    if int_weight <= 0 or  type(int_weight) is not int:
        print('Please add some number weight value')
    else:
        standard_val = input('What is the standard of your weight kilograms(K) or Pounds(L)? ').strip()
        if len(standard_val)==0 :
            print('Please add some value')
        else:
            if standard_val.lower().startswith('k'):
                user_weight = f'{int_weight /0.45} pounds'
            elif standard_val.lower().startswith('p') or standard_val.lower()[0] == 'l':
                user_weight = f'{int_weight*0.45} kgs'
            else:
                print('Please add some reasonable weight')
            print(f'Your weight is {user_weight}')  
    break              