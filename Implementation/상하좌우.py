n=int(input())
ar=input().split()
locate=[1,1]

for i in ar:
    if i=='R' and locate[1]!=n:
        locate[1]+=1
    if i=='L' and locate[1]!=1:
        locate[1]-=1
    if i=='U' and locate[0]!=1:
        locate[0]-=1
    if i=='D' and locate[0]!=n:
        locate[0]+=1

print(locate[0],locate[1])