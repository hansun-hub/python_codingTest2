n = int(input())
a = input().split()

for i in range(n):
    a[i]=int(a[i])

d=[]
#리스트 생성 잘했다.
for i in range(24):
    d.append(0)

#아직 리스트에는 몇개 있다 정의가 없는 상태
#따라서 append함수로 해줘야 한다.

for i in range(n):
    d[a[i]]+=1

for i in range(1, 24):
    print(d[i], end=' ')




