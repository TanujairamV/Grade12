### Write a Python program to create a binary file student.dat that stores the data (roll number, name, marks) of 5 students
import pickle
f = open('student.dat', 'wb')  # Open the file in binary write mode
for i in range(5):
    roll = int(input("Enter roll number: "))  # Get roll number from user
    name = input("Enter name: ")  # Get name from user
    marks = float(input("Enter marks: "))  # Get marks from user
    student = (roll, name, marks)  # Create a tuple for the student data
    pickle.dump(student, f)  # Write the student data to the binary file
f.close()  # Close the file after writing

### Write a Python program to search the roll number and display the name and marks of the student.Structure:[roll number, name, marks]
import pickle
f = open('student.dat', 'rb')  # Open the file in binary read mode
roll_to_search = int(input("Enter roll number to search: "))  # Get roll number
try:
    while True:  # Loop until EOFError is raised
        student = pickle.load(f)  # Load the student data from the file
        if student[0] == roll_to_search:  # Check if the roll number matches
            print(f"Name: {student[1]}, Marks: {student[2]}")  # Display name and marks
except EOFError:
    f.close()  # Close the file after reading
    
### Function updatefare() to increase a fare by 10% in a binary file
import pickle
def updatefare():
    try:
        f = open(student.dat, 'rb+')  # Open the file in binary read mode
        while True:
            position = f.tell()
            d = pickle.load(f)
            d[4] += d[4] * 0.10
            f.seek(position)  # Move the file pointer to the current position
            pickle.dump(d, f)  # Write the updated data back to the file
    except EOFError:
        f.close()
            
        