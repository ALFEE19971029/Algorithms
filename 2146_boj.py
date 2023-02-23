import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

candidate = set()

def checkEdge(x,y,cnt):
    visited = [[False]*N for _ in range(N)]
    visited[x][y] = True
    arr[x][y] = cnt
    queue = deque([])
    queue.append((x,y))
    while queue:
        ox,oy = queue.popleft()
        for i in range(4):
            nx = ox + dx[i]
            ny = oy + dy[i]
            if 0<=nx<=N-1 and 0<=ny<=N-1 and visited[nx][ny] == False:
                if arr[nx][ny] == 1:
                    visited[nx][ny] = True
                    arr[nx][ny] = cnt
                    queue.append((nx,ny))
                elif arr[nx][ny] == 0:
                    candidate.add((ox,oy,cnt))
cnt = 2

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            checkEdge(i,j,cnt)
            cnt += 1

minVal = 1e10

def findShortest(x,y,cnt):
    global minVal
    visited = [[0]*N for _ in range(N)]
    visited[x][y] = 1
    queue = deque([])
    queue.append((x,y))
    while queue:
        ox,oy = queue.popleft()
        for i in range(4):
            nx = ox + dx[i]
            ny = oy + dy[i]
            if 0<=nx<=N-1 and 0<=ny<=N-1 and visited[nx][ny] == 0 and arr[nx][ny] != cnt:
                if minVal <= visited[ox][oy]:
                    return
                if arr[nx][ny] != 0:
                    minVal = visited[ox][oy]
                    return
                visited[nx][ny] = visited[ox][oy] + 1
                queue.append((nx,ny))

for i in candidate:
    findShortest(i[0],i[1],i[2])

print(minVal-1)
     