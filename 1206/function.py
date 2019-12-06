def sum():
    return "hi"

print(sum())

def multiplyAndDivide(a,b):
    multiplyResult=a*b
    divideResult=a/b
    return multiplyResult, divideResult

result=multiplyAndDivide(12,6)
print(type(result))  #튶튜플

