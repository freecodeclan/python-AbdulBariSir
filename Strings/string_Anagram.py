# Check if two strings are Anagram

s1 = input('Enter a string\n')
s2 = input('Enter a second string\n')

if len(s1) != len(s2):
    print('Not Anagaram')

else:

    for x in s1:
        if x not in s2:
            print('Not Anagram')
            break
    else:
        print("It's Anagram")