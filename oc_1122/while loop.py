sum=0
n=0

while n<11:
    sum=sum+n
    n=n+1

print(sum)

n=0
while n<10:
    n=n+1
    if n==3:
        continue
    if n==5:
        break
    print("현재 n은 " + str(n) + "입니다")

names=['신봉건', '고유빈', '김진옥', '이광우']
nimNames =[]

for name in names:
    nimNames.append(name+"님")

for nimName in nimNames:
    print(nimName)

print("================")

nimNames2= [name+"님" for name in names]

for nimName in nimNames2:
    print(nimName)