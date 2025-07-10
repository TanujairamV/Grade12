#Opening the file in python

##Modes
#For txt files, the modes are:
# 'r'  - Read mode (default). File must exist.
# 'w'  - Write mode. Creates file if not exists, truncates if it does.
# 'a'  - Append mode. Creates file if not exists, appends if it does.
#For dat files(binary files), the modes are:
# 'rb' - Read mode for binary files. File must exist.
# 'wb' - Write mode for binary files. Creates file if not exists.
# 'ab' - Append mode for binary files. Creates file if not exists - Always use 'ab' for writing binary files.

#Opening the file
#Method 1: Using open() close()
f = open('tfile.txt', 'r')  # Must close the file manually using f.close()
f.close()
#Method 2: Using 'with' statement
with open('tfile.txt', 'r') as f:  # Automatically closes the file after block execution, should write with intentation

#Absolute path
with open('C:/programs/tfile.txt', 'r') as f:  # Use absolute path to specify the file location from the root directory

#Relative path
with open('tfile.txt', 'r') as f:  # Use relative path to specify the file location, relative to the current working directory
    