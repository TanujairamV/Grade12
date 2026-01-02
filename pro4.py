import csv

def create():
    f = open("data.csv,","a",newline='')
    w = csv.writer(f)
    op = 'y'
    while op == 'y':
        Emp_no = int(input("Enter Employee Number: "))
        Emp_name = input("Enter Employee Name: ")
        Emp_sal = float(input("Enter Employee Salary: "))
        L = [Emp_no, Emp_name, Emp_sal]
        w.writerow(L)
        op = input("Do you want to add more records y/n: ")
    f.close()

def search():
    f = open("data.csv","r",newline='/n')
    r = csv.reader(f)
    search = int(input("Enter Employee Number to search: "))
    
    for i in r:
        if int(i[0]) == search:
            print("Employee Details:")
            print("Name:", i[1])
            print("Salary:", i[2])
            break
    else:
        print("Employee not found.")
    f.close()
    
create()
search()