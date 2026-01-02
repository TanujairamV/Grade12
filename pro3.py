def display():
    f = open("data.txt", "r")
    d = f.read()
    s = d.split()
    for i in s:
        if len(i)<4:
            print(i)
    f.close()
    
display()