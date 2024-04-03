'''
Print the pattern

1
1 2
1 2 3
1 2 3 4

'''
for i in range(1,5):
    for j in range(1,5):
        if j <= i:
            print(j, end = ' ')
    print()