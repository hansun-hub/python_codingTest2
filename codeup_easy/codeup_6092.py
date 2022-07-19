n=int(input())
a=input().split()
#split() 적어준다. 배열이 되겠지?

for i in range(n):
    a[i]=int(a[i])
#int로 만들어줌
#배열에 들어있는 것들을

d=[]
#리스트 생성
for i in range(24):
    d.append(0)
#1부터 23까지 0으로 넣어줌

for i in range(n):
    #d[a[i]]+=1
    d[a[i]]=d[a[i]]+1

#1부터 n 그니까 10번 반복
#0을 넣어줬었는데 한 번 나오면 1더하고 더 나오면 1더하고 한다

for i in range(1,24):
    print(d[i],end=' ')
#1부터 23까지 반복해서
#배열 d출력해준다.
