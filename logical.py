# and or 
# they are used conditionals and logics
has_hight_income = True
has_good_credit = False
has_criminal_record = False


if has_hight_income or has_good_credit:
    print('Is eligible for credit')

#not 
if has_good_credit and not has_criminal_record:
    print('Applicant also eligible for loan') 
    