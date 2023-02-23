import sys
sys.setrecursionlimit(10**9)

N = int(input())

graph = []
boolArr = [] 
cntArr = []
cnt = 0
dx = [0,0,-1,1]
dy = [1,-1,0,0]

for _ in range(N):
    graph.append(list(map(int,input().split())))

maxVal = max(max(x) for x in graph)

def dfs(x,y):
    global boolArr, cnt
    boolArr[y][x] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx > N-1 or ny < 0 or ny > N-1 or boolArr[ny][nx] == True:
            continue
        else:
            dfs(nx,ny)


for i in range(0,maxVal+1):
    boolArr = [[False]*N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if graph[y][x] <= i:
                boolArr[y][x] = True
    for y in range(N):
        for x in range(N):
            if boolArr[y][x] == True:
                continue
            else:
                cnt += 1
                dfs(x,y)

    cntArr.append(cnt)            
    cnt = 0
    
print(max(cntArr))
