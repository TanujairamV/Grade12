def count():
    f = open("data.txt", "r")
    d = f.read()
    v = c = l = u = 0
    
    for i in d:
        if i.isalpha():
            if i.lower() in "aeiou":
                v+=1
            else:
                c+=1
            if i.islower():
                l += 1
            else:
                u += 1
                
    print("Vowels:", v)
    print("Consonants:", c)
    print("Lowercase letters:", l)
    print("Uppercase letters:", u)

count()