def calc(calctype, a, b):
    if calctype=='더하기':
        return a+b
    elif calctype=='빼기':
        return a-b
    elif calctype=='곱하기':
        return a*b
    elif calctype=='나누기':
        return a/b

a = input("계산정보를 입력하세요: ")
b=a.split()

result = calc(b[0], int(b[1]), int(b[2]))
print("계산결과 : " + str(result))
