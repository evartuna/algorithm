pos=input()
x=pos[0]
y=int(pos[1])
cnt=8

if y==2 or y==7:
    cnt-=2
if y==1 or y==8:
    cnt-=4

if x=='a' or x=='h':
    cnt-=4
if x=='b' or x=='g':
    cnt-=2

if pos=='a1' or pos=='h1' or pos=='h8' or pos=='a8':
    cnt=2
print(cnt)