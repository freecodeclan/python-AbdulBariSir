# File Handling in Python
File handling in Python refers to the process of working with files on your computer's filesystem. Python provides built-in functions and methods for creating, reading, writing, and manipulating files.

The key function for working with files in Python is the **open( )** function. The **open( )** function takes two parameters; filename, and mode.

    file = open('file_name', 'r')

There are four different methods (modes) for opening a file:

**"r" - Read -**  Default value. Opens a file for reading, error if the file does not exist

**"a" - Append -** Opens a file for appending, creates the file if it does not exist

**"w" - Write -** Opens a file for writing, creates the file if it does not exist

**"x" - Create -** Creates the specified file, returns an error if the file exists

**"w+" - Write and Read -** This mode opens the file for both reading and writing. The text is overwritten and deleted from an existing file. The start of the file is where the handle is located.

**"a+" - Append and Read -** Using this method, you can read and write in the file. If the file doesn't already exist, one gets created. The handle is set at the end of the file. The newly written text will be added at the end, following the previously written data.

**"r+" - Read and Write -**  This method opens the file for both reading and writing. The start of the file is where the handle is located. If the file does not exist, an I/O error gets raised.

