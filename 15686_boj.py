import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int,input().split())
city = [list(map(int,input().split())) for _ in range(N)]
houseXY = deque([])
chickenXY = deque([])
ans = 1e9

for i in range(N):
    for j in range(N):
        if city[i][j] == 0:
            continue
        elif city[i][j] == 1:
            houseXY.append((j,i))
        elif city[i][j] == 2:
            chickenXY.append((j,i))

temp = deque([])

def dfs(depth,index):
    global ans
    if depth == M:
        localMin = 1e9
        sum = 0
        for xy in houseXY:
            for c in temp:
                localMin = min(localMin,abs(xy[0]-c[0])+abs(xy[1]-c[1]))
            sum += localMin
            localMin = 1e9
        ans = min(ans,sum)
        return
    for i in range(index, len(chickenXY)):
        temp.append(chickenXY[i])
        dfs(depth+1,i+1)
        temp.pop()

dfs(0,0)
print(ans)

