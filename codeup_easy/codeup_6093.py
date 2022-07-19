n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])

d=[]
for i in range(n):
    d.append(0)

for i in range(n):
    d[i]=d[i]+a[i]
#입력한 만큼 for문 도는 것

for i in range(n-1,-1,-1):
    print(d[i], end=' ')


