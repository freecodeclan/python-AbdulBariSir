# Creating Dictionary

car_Company = {'Hyundai': 'Verna', 'Mahindra': 'Thar', 'Skoda': 'Slavia', 'Porsche': 'Panamera'}
print(car_Company)
print()
car_Name = dict({'Verna': 'grey', 'Slavia': 'Blue', 'Porsche': 'Cherry Red'})
print(car_Name)

del car_Name['Verna']
print(car_Name)

print()

# Iteration on Dictionary 
print()
for key, value in car_Name.items():
    print(key, ':', value)

print()

for i in car_Company:
    print(i, car_Company[i])

# Accessing items by using get()
x = car_Company.get('Hyundai')
print(x)

# Accessing all keys() of Dictionary
x = car_Company.keys()
print(x)

print()

# Accessing all values of Dictionary
x = car_Company.values()
print(f'The values are as follow {x}')

print()

# Accessing all items of Dictionary
x = car_Company.items()
print(f'The items in dictionary are as follow {x}')

print()

# Adding items to Dictionary
car_Name['LandRover'] = 'Metallic Black'
car_Name.update({'Defender': 'Off-white', 'Lexus': 'Grey', 'Ferrari': 'BloodRed'})  # Adding multiple items in Dictionary
print(car_Name)

print()
# Now removing last inserted item of Dictionary
car_Name.popitem()
print(car_Name)


# Using zip() Method to make key : value pair
L1 = ['a', 'b', 'c']
L2 = ['apple', 'ball', 'cat']

dict_New = dict(zip(L1,L2))
print(dict_New)