def display():
    f = open("data.txt", "r")
    d = f.readlines()
    
    for i in d:
        s = i.strip()
        for j in s:
            print(j+"#")
        print()
    f.close()

display()