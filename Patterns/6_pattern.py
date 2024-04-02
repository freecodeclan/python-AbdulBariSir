'''
Print the pattern

* * * * * * *
  * * * * *
    * * *
      *

'''
for i in range(1,5):
    for j in range(1,8):
        if j >= i and j <= 5-i+3:
            print('*', end = ' ')
        else:
            print(' ', end = ' ')
    print()