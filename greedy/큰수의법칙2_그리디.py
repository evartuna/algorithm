n,m,k= map(int,input().split())
data=list(map(int,input().split()))

data.sort()

first=data[n-1]
second=data[n-2]

result=0

cnt=m//(k+1)*k
cnt+=m%(k+1)

result=cnt*first+(m-cnt)*second
print(result)