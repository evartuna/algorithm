n=int(input())
array=[]
for i in range(n):
    array.append(input().split())

def order(arr):
    return arr[0]

array.sort(key=order)

for i in array:
    print(i[0],end=' ')