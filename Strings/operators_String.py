# Opearators on String

# 1.. Concatenation 

car1 = "Hyundai "
car2 = "Verna"

print(car1 + car2)  # By using addition + symbol we concatenate two strings

# To concatenate String with integer we need to uise data type before int to convert into string
car2 = 'verrna ' + str(1500)
print(car2)

# Indexing
car = "Defender V110"
for i in range(0, len(car)):
    print(car[i], end = ' ')

print()

# Slicing
name = "GODRAMA"
sliced_name = name[1:5]
print(sliced_name)

