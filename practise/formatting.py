firstname = 'Abdulhakim'
lastname = 'Maha'
age = 19
salary = 500.1234

# approach 1
print('Your name is {} {} and {} years old and salary {:.2f}'.format(firstname, lastname, age, salary))

# approach 2
print('Your name is %s %s %d %.2f' %(firstname, lastname, age, salary))