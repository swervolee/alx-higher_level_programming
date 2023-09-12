#                   Python File Input and Output Guide
=======================================================================

Table of Contents

    * Introduction
    * Reading from Files
    * Opening a File
    * Reading Methods
    * Writing to Files
    * Opening a File for Writing
    *  Writing Methods
    * Closing Files
    * Exception Handling
    * Conclusion

## Introduction

Working with files is a fundamental part of many programming tasks, and Python provides a simple and powerful way to perform file input and output operations. This guide will walk you through the basics of reading from and writing to files in Python.
Reading from Files
Opening a File

To read data from a file in Python, you first need to open the file using the built-in open() function. The open() function takes two arguments: the file path and the mode in which you want to open the file. Common file modes for reading are:

    "r": Read mode (default) - opens the file for reading.
    "rb": Binary read mode - for reading binary files.

Example of opening a file for reading:

python

## Open a text file for reading
file_path = "example.txt"
with open(file_path, "r") as file:
    # Your file reading code here

## Reading Methods

Once you've opened a file, you can read its contents using various methods. Some common ones include:

    read(): Reads the entire file as a single string.
    readline(): Reads one line at a time.
    readlines(): Reads all lines into a list of strings.

Example of reading from a file:

python

#### Open a text file for reading
file_path = "example.txt"
with open(file_path, "r") as file:
    content = file.read()
    #### Process the content here

## Writing to Files
Opening a File for Writing

To write data to a file in Python, you need to open the file in write mode using the "w" mode. Be cautious when opening a file in write mode, as it will overwrite the file's existing content.

## Example of opening a file for writing:

python

# Open a text file for writing
file_path = "output.txt"
with open(file_path, "w") as file:
    # Your file writing code here

## Writing Methods

After opening a file for writing, you can use methods like write() to add content to the file. Remember to close the file after writing to save the changes.

Example of writing to a file:

python

### Open a text file for writing
file_path = "output.txt"
with open(file_path, "w") as file:
    file.write("Hello, world!\n")
    file.write("This is a new line of text.")

## Closing Files

It's essential to close files properly using the with statement or the close() method to free up system resources and ensure data integrity.

python

### Using with statement automatically closes the file when done
with open(file_path, "r") as file:
    content = file.read()
### File is automatically closed here

## Exception Handling

When working with files, it's a good practice to handle exceptions gracefully. Common exceptions include FileNotFoundError (when the file doesn't exist) and PermissionError (when you don't have permission to access the file). You can use try...except blocks to handle these exceptions.

python

try:
    with open(file_path, "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("Permission denied!")

## Conclusion

Python provides a straightforward and versatile way to work with file input and output. By understanding the concepts outlined in this guide, you'll be well-equipped to read from and write to files in your Python projects. Remember to handle exceptions and close files properly for robust and reliable file operations. Happy coding!
