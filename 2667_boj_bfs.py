import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [list(map(int,input().rstrip())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]

dx=[0,0,-1,1]
dy=[1,-1,0,0]

def bfs(x,y):
    cnt = 1
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0
    while queue:
        ox,oy = queue.popleft()
        for i in range(4):
            nx = ox + dx[i]
            ny = oy + dy[i]
            if 0<=nx<=N-1 and 0<=ny<=N-1 and graph[nx][ny] == 1:
                queue.append((nx,ny))
                graph[nx][ny] = 0
                cnt += 1
    return cnt

danjiCnt = 0
cntArr = []

for i in range(N):
    for j in range(N):
        if graph[i][j]:
            cntArr.append(bfs(i,j))
            danjiCnt += 1

print(danjiCnt)
cntArr.sort()
for i in range(danjiCnt):
    print(cntArr[i])
