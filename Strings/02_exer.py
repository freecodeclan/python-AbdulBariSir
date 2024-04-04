'''
Display data in given format

Chicken Pizza..........300

'''
item_Name = input("Enter the item name: ")
price = input("Enter the price for an item: ")

total_len = len(item_Name) + len(price)

print(total_len)

dots = '.' * (25 - total_len)

print(item_Name+dots+price)