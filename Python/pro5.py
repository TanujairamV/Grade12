import pickle

def create():
    f = open("students.dat", "ab")
    op = 'y'
    while op == 'y':
        roll = int(input("Enter Roll Number: "))
        name = input("Enter Name: ")
        L = [roll, name]
        pickle.dump(L, f)
        op = input("Do you want to add more records y/n: ")
    f.close()
    
def search():
    f = open("students.dat", "rb")
    search = int(input("Enter Roll Number to search: "))
    try:
        while True:
            L = pickle.load(f)
            if L[0] == search:
                print("Student Details:",L)
                break
        else:
            print("Student not found.")
    except:
        f.close()

create()
search()