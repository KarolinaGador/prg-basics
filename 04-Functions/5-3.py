###
# Allows to enter and print employee data. Due to personal
# data protection, you can determine whether information about
# the employee's salary will be printed
#
import keyboardd # your own defined module

# Reads employee's data from keyboard
first_name = keyboardd.input_string('Enter name: ')
last_name = keyboardd.input_string('Enter name: ')
age = keyboardd.input_integer('enter age: ')
salary = keyboardd.input_integer('enter salary:')
is_salary_hidden = keyboardd.input_boolean('Hide salary? (y/n)')

# Prints employee's record
print('DATA RECORD')
print('===========')
print(f'Name:', {first_name})
print(f'Last:', {last_name})
print(f'Age:', {age})
if is_salary_hidden==False:
    print(f'{salary}')