# .csv is the file extension for Comma-Separated Values files.
# Default delimiter is a comma ,
# Should import the csv module to work with CSV files
import csv

#Reading a CSV file
with open('CSV file//students.csv', 'r') as f:
    reader = csv.reader(f)
    for i in reader:               #Must iterate through the reader object to get each row
        print(i)
##Output
#['Alice', '101', '87']
#['Bob', '102', '91']
#['Charlie', '103', '78']

#Writing to a CSV file
#writerow() method is used to write a single row to the CSV file.
with open('CSV file//students_new.csv', 'w', newline='') as f:  #newline='' prevents extra blank lines
    writer = csv.writer(f)
    writer.writerow(['Name', 'ID', 'Score'])
    writer.writerow(['Alice', '101', '87'])
    writer.writerow(['Bob', '102', '91'])
    writer.writerow(['Charlie', '103', '78'])
    
#writerows() method is used to write multiple rows at once.
#Using nested lists(Same for tuples)
with open('CSV file//students_new.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerows([['David', '104', '85'],['Eve', '105', '92']])
#Using a list of dictionaries - Only the keys will be added
with open('CSV file//students_custom.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter=';')
    d = {'Name': 'Alice', 'Age': 23, 'Grade': 'A'}
    writer.writerow(d)  # Writing a single row with custom delimiter
    
#Adding custom delimiter
writer = csv.writer(f, delimiter=';')  # Using semicolon as delimiter
    



