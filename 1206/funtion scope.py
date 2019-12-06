a=2

def changeA():
    a=3
    return a

def changeGlobalA():
    global a
    a=3
    
b=changeA()
changeA()
print(a)