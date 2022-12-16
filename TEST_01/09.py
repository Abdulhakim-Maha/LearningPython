id = int(input('Enter your id: '))
name = input('Enter your name: ')
salary = int(input('Enter your salary: '))
if salary > 50000 : salary = salary - salary * 0.1
else: salary = salary - salary * 0.05
print(salary)