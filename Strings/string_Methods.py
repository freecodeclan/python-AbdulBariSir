company = 'Maruti'

print(dir(company)) # dir(str) used see all the in-built methods of String Class

help(company.rjust) # By using help() function we can read about the functionality of methods

s = "Hello, how are you"

print(s.find('how')) # The find() method finds the first occurrence of the specified value and it returns -1 if value is not found

print(s.count('o')) #Returns the number of times a specified value occurs in a string

mail = "harshmehra53@gmail.com"
new_mail = mail.replace('gmail', 'yahoo')   # The replace() method replaces a specified phrase with another specified phrase.
print(new_mail)

print()

s1 = '/'
s2 = 'Hello World'
s3 = s1.join(s2)    #The join() method takes all items in an iterable and joins them into one string.
print(s3)

print()

greet = 'Hello very good morning'
new_str = greet.split() #The split() method splits a string into a list.

print(new_str)