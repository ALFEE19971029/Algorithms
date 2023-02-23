import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N = int(input())

people = [0] + list(map(int,input().split()))

connected = [[] for _ in range(N+1)]

for _ in range(N-1):
    x, y = map(int,input().split())
    connected[x].append(y)
    connected[y].append(x)

dp = [[0,0] for _ in range(N+1)]
visited = [False]*(N+1)

def dfs(start):
    visited[start] = True
    dp[start][0] = 0
    dp[start][1] = people[start]
    for i in connected[start]:
        if visited[i] == False:
            dfs(i)
            dp[start][0] += max(dp[i][0],dp[i][1])
            dp[start][1] += dp[i][0]
        
dfs(1)

print(max(dp[1][0], dp[1][1]))


