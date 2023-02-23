N = int(input())

graph = []
cnt = 0
cntArr = []
danjiCnt = 0
dx = [0,0,-1,1]
dy = [1,-1,0,0]

for _ in range(N):
    graph.append(list(map(int,input())))

def dfs(x,y):
    global graph, cnt, dx, dy
    cnt += 1
    graph[y][x] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx > N-1 or ny < 0 or ny > N-1 or graph[ny][nx] == 0:
            continue
        else:
            dfs(nx,ny)

for i in range(N):
    for j in range(N):
        if graph[i][j] == 0:
            continue
        else:
            dfs(j,i)
            cntArr.append(cnt)
            cnt = 0
            danjiCnt += 1

print(danjiCnt)
cntArr.sort()
for i in range(danjiCnt):
    print(cntArr[i])