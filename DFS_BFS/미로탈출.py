from collections import deque

n,m=map(int,input().split())
graph=[]
visited=[[False]*m for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

for i in range(n):
    graph.append(list(map(int,input())))
    

def bfs(x,y,visited):
    queue=deque()
    queue.append((x,y))

    while queue:
        x,y=queue.popleft()
        visited[x][y]=True
        if x==4 and y==5:
            break
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<=-1 or nx>=n or ny<=-1 or ny>=m :
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))
        
    return graph[n-1][m-1]




print(bfs(0,0,visited))