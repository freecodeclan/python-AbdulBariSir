# File Handling in Python
File handling in Python refers to the process of working with files on your computer's filesystem. Python provides built-in functions and methods for creating, reading, writing, and manipulating files.

The key function for working with files in Python is the **open( )** function. The **open( )** function takes two parameters; filename, and mode.

    file = open('file_name', 'r')

There are four different methods (modes) for opening a file:

**"r" - Read -**  Default value. Opens a file for reading, error if the file does not exist

**"a" - Append -** Opens a file for appending, creates the file if it does not exist

**"w" - Write -** Opens a file for writing, creates the file if it does not exist

**"x" - Create -** Creates the specified file, returns an error if the file exists
