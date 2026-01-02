Stack = []

def push():
    id = input("Enter the id: ")
    name = input("Enter the name: ")
    spl = input("Enter the specialization: ")
    if spl == "ENT":
        Stack.append([id, name])
        
def pop():
    if Stack == []:
        print("Stack is empty")
    else:
        print("Popped element:", Stack.pop())

def peek():
    if Stack == []:
        print("Stack is empty")
    else:
        print("Top element:", Stack[-1])
        
def display():
    if Stack == []:
        print("Stack is empty")
    else:
        for i in Stack[::-1]:
            print(i)

op = 'y'

while op == 'y':
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        peek()
    elif choice == 4:
        display()
    else:
        print("Invalid choice")
        
    op = input("Do you want to continue y/n: ")    
