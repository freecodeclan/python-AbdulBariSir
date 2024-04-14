file = open('practice.txt','w')     # created new file using write mode

file.write('Hello I am just a practice file\n')     # Adding content in file while creating new file
file.write('I am on trial phase\n')

file.close()

# Checking the status of file
print(file.name)    # used to check the name of the file 
print(file.mode)    # used to check the mode of the file
print(file.closed)  # # used to check the status of the file is opened or closed and it return boolean value

file = open('practice.txt','a')     # Now we are in append mode 

file.write('Welcome back again\n')  # adding content into existing file again
file.write('I am in append phase\n')

print(file.closed)

file.close()        # closing file again








