n=1260
ar=[500,100,50,10]
cnt=0

for i in ar:
    cnt+=n//i
    n%=i

print(cnt)