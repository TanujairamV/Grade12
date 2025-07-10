# .txt is the extension for text files

# Reading from a file
d = f.read()  # Read the entire file
d = f.read(10)  # Read the first 10 characters
d = f.readline()  # Read one line from the file
d = f.readlines()  # Read all lines into a list (Output: ['line1\n', 'line2\n'])

# Writing to a file
f.write('Hello World')  # Write a string to the file
f.writelines(['Hello\n', 'World\n'])  # Write a list of strings

#Flush - writes to the file immediately rather than waiting for the file to close
f.flush()  # Flush the write buffer to the file

