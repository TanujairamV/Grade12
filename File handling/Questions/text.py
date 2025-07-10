### Read and display the words less than 4 characters from a text file
f = open('tfile.txt', 'r')  
words = f.read()
s = words.split()  # Split the content into words
for i in s:
    if len(i) < 4:  
        print(i)  
f.close()  


### Number of times a word "the" appears in a text file
f = open('tfile.txt', 'r')  
words = f.read()
s = words.split()  # Split the content into words
for i in s:
    if i.lower() == 'the':  # Check if the word is "the"
        print(i)  # Print the word
f.close()  # Close the file after reading


### Word starting with 'a' in a text file
f = open('tfile.txt', 'r')  
words = f.read()
s = words.split()  # Split the content into words
for i in s:
    if i[0] == 'a' or i[0] == 'A':  # Check if the word starts with 'a' or 'A'
        print(i)  # Print the word
f.close()  # Close the file after reading
        
        
### Display unique words
f = open('tfile.txt', 'r')  # Open the file in read mode
words = f.read()
s = words.split()  # Split the content into words
unique_words = []  # Use a set to store unique words
for i in s:
    if i not in unique_words:  # Check if the word is not already in the list
        unique_words.append(i)  # Add the word to the list
print(unique_words)  # Print the list of unique words
f.close()  # Close the file after reading


### Get the input sentence and wite it to a file
f = open('tfile.txt', 'w')  # Open the file in write mode
n = int(input("Enter the number of lines: "))  # Get the number of lines from user
for i in range(n):
    s = input("Enter the sentence: ")  # Get the sentence from user
    f.write(s)  # Write the sentence to the file with a newline character
f.close()  # Close the file after writing

### Replace "a" with "an" in a text file
f = open('tfile.txt', 'r')
words = f.read()
f.close()  # Close the file after reading
f = open('tfile.txt', 'w')  # Open the file in write mode
d = words.replace(' a ', ' an ')  # Replace " a " with " an "
f.write(d)  # Write the modified content back to the file
f.close()  # Close the file after reading

