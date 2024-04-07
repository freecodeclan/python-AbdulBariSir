# Creating List
car_Name = ['Verna', 'i20', 'Creta', 'i10','Slavia', 'Virtus']

# Slicing List
car_List = car_Name[0:5]    # [starting_Index_Value, end_Index_Value]
print(car_List)

# Concatinating List -- But in concatination python return new list 
car_Company = ['Hyundai', 'Maruti', 'Skoda', 'Volkswagen', 'BMW']

car_List1 = car_Name + car_List
print(car_List1)

# To expand the list we can use extend function this will modify the original list
car_Name.extend(['Panamera', 'Defender', 'Thar'])
print(car_Name)