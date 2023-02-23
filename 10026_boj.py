
import sys
sys.setrecursionlimit(10**9)
N = int(input())

graph = []
graph2 = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def convertRtoG(elem):
    if elem == 'R':
        return 'G'
    else:
        return elem

for _ in range(N):
    list_oneline = list(input().rstrip())
    graph.append(list_oneline)
    graph2.append(list(convertRtoG(x) for x in list_oneline))

cnt1 = 0
cnt2 = 0

def dfs(x,y,graph):
    global dx, dy
    temp = graph[y][x]
    graph[y][x] = 'C'
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx > N-1 or ny < 0 or ny > N-1 or graph[ny][nx] != temp:
            continue
        else:
            dfs(nx,ny,graph)

for i in range(N):
    for j in range(N):
        if graph[i][j] == 'C':
            continue
        else:
            cnt1 += 1
            dfs(j,i,graph)

for i in range(N):
    for j in range(N):
        if graph2[i][j] == 'C':
            continue
        else:
            cnt2 += 1
            dfs(j,i,graph2)

print(cnt1, cnt2)