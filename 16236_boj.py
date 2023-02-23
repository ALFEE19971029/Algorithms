import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

space = [list(map(int,input().split())) for _ in range(N)]

dx = [0,-1,1,0]
dy = [1,0,0,-1]

startX = 0
startY = 0

breaker = False

for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            startX = i
            startY = j
            breaker = True
            break
    if breaker == True:
        break

def bfs(x,y,size):
    visited = [[0]*N for _ in range(N)]
    queue = deque([(x,y)])
    space[x][y] = 0
    visited[x][y] = 1
    ateArr = []
    while queue:
        ox, oy = queue.popleft()
        for i in range(4):
            nx = ox + dx[i]
            ny = oy + dy[i]
            if 0<=nx<=N-1 and 0<=ny<=N-1 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[ox][oy] + 1
                if space[nx][ny] == 0:
                    queue.append((nx,ny))
                elif space[nx][ny] < size:
                    ateArr.append((nx,ny))
                elif space[nx][ny] == size:
                    queue.append((nx,ny))
                elif space[nx][ny] > size:
                    continue
    if ateArr:
        ateArr.sort(key= lambda x:(visited[x[0]][x[1]],x[0],x[1]))
        space[ateArr[0][0]][ateArr[0][1]] = 0
        return (ateArr[0],visited[ateArr[0][0]][ateArr[0][1]]-1,True)
    else:
        return ((),None,False)

x, y = startX, startY

sharkStatus = [2,0]
moveCnt = 0

while True:
    if sharkStatus[0] == sharkStatus[1]:
        sharkStatus[0] += 1
        sharkStatus[1] = 0
    result = bfs(x,y,sharkStatus[0])
    if result[2] == False:
        break
    moveCnt += result[1]
    x, y = result[0]
    sharkStatus[1] += 1

print(moveCnt)


                   
