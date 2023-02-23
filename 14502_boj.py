import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

N, M = map(int,input().split())
dx = [0,0,1,-1]
dy = [1,-1,0,0]

maxVal = 0
zeroCnt = 0

arr = [list(map(int,input().split())) for _ in range(N)]

zeroLocations = []

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            zeroCnt += 1
            zeroLocations.append((i,j))

def bfs(x,y):
    changedVal = 0
    queue = deque()
    queue.append((x,y))
    visited.add((x,y))
    while queue:
        ox,oy = queue.popleft()
        for i in range(4):
            nx = ox + dx[i]
            ny = oy + dy[i]
            if 0<= nx <= N-1 and 0<= ny <= M-1 and arr[nx][ny] == 0 and (nx,ny) not in visited:
                queue.append((nx,ny))
                visited.add((nx,ny))
                changedVal += 1
    return changedVal

visited = set()
zeroCnt -= 3

for threePoints in combinations(zeroLocations,3):
    tempCnt = 0
    x1,y1 = threePoints[0]
    x2,y2 = threePoints[1]
    x3,y3 = threePoints[2]
    arr[x1][y1] = 1
    arr[x2][y2] = 1
    arr[x3][y3] = 1
    for i in range(N):
        for j in range(M):
            if (i,j) not in visited and arr[i][j] == 2:
                tempCnt += bfs(i,j)
    visited = set()
    maxVal = max(maxVal, zeroCnt-tempCnt)
    arr[x1][y1] = 0
    arr[x2][y2] = 0
    arr[x3][y3] = 0

print(maxVal) 