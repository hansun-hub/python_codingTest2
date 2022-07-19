a,m,d,n=input().split()
a=int(a)
m=int(m)
d=int(d)
n=int(n)

for i in range(1,n):
    a=a*m
    a=a+d
print(a)
