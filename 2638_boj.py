import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]


def bfs(x,y):
    isCheeze = False
    visited = [[False]*M for _ in range(N)]
    visited[x][y] = True
    meltCheck = [[0]*M for _ in range(N)]
    meltLocation = set()
    queue = deque()
    queue.append((x,y))
    while queue:
        ox,oy = queue.popleft()
        for i in range(4):
            nx = ox + dx[i]
            ny = oy + dy[i]
            if 0<= nx <= N-1 and 0<= ny <= M-1 and visited[nx][ny] == False:
                if arr[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                elif arr[nx][ny] == 1:
                    isCheeze = True
                    meltCheck[nx][ny] += 1
                    if meltCheck[nx][ny] == 2:
                        meltLocation.add((nx,ny))
    for i in meltLocation:
        arr[i[0]][i[1]] = 0
    return isCheeze

cnt = 0
while True:
    if not bfs(0,0):
        break
    cnt += 1

print(cnt)
            