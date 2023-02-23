import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N, M = map(int,input().split())
candies = []

for i in range(N+1):
    if i == 0:
        candies.append([0]*(M+1))
    else:
        candies.append([0] + list(map(int,input().split())))

for i in range(1,N+1):
    for j in range(1,M+1):
        candies[i][j] = max(candies[i-1][j-1], candies[i-1][j], candies[i][j-1]) + candies[i][j]

print(candies[N][M])

#dfs
"""
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N, M = map(int,input().split())
candies = [list(map(int,input().split())) for _ in range(N)]
maxVal = 0
dx = [0,1,1]
dy = [1,0,1]

#sumval 값 주의
def dfs(x,y,sumVal):
    global maxVal
    if x == N-1 and y == M-1:
        if sumVal > maxVal:
            maxVal = sumVal
    
    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx <= N-1 and 0<= ny <= M-1:
            dfs(nx,ny,sumVal + candies[nx][ny])

dfs(0,0,candies[0][0])

print(maxVal)
"""