n = int(input())
a = input().split()

b=0
for i in range(n):
    a[i] = int(a[i])

b=a[0]
for i in range(1,n):
    if b>a[i]:
        b=a[i]
print(b)

