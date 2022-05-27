n=int(input())
array=[]
for i in range(n):
    inputd=input().split()
    array.append((inputd[0],int(inputd[1])))
ma=1
for i in array:
    if ma<i[1]:
        ma=i[1]
gs=[0]*(ma+1)

for i in array:
    gs[i[1]]+=1

for i in range(len(gs)):
    for j in range(gs[i]):
        for k in array:
            if i==k[1]:
                print(k[0],end=' ')