# From the given list print only those numbers who's remainder is 0 when divided by 2.

list1 = [int(x) for x in input('Enter the numbers: ').split()]

new_list = list(filter(lambda x: x % 2 == 0, list1))

print(new_list)




