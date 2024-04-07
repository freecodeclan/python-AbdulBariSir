# Calculate Salary, weekly working hours given in list

working_hours = [int(x) for x in input('Enter hrs per day in entier week, seprated by space: ').split()]    # using list comprehension

wage = int(input('Enter hourly wage: '))

total_hrs = sum(working_hours)

salary = total_hrs * wage

print('Salary is',salary)


