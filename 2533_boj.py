import sys
input = sys.stdin.readline

N = int(input())

edge = [[] for _ in range(N+1)]

for _ in range(N-1):
    x, y = map(int,input().split())
    edge[x].append(y)

level = [[] for _ in range(N+1)]


level[1].append(1)
deepestLevel = 0

for i in range(1,N):
    for j in level[i]:
        for k in edge[j]:
            level[i+1].append(k)
            deepestLevel = i+1

dp = [[0,0] for _ in range(deepestLevel+1)]

dp[2][0] = 1
dp[2][1] = len(level[2])

for i in range(3,deepestLevel+1):
    dp[i][1] = dp[i-1][0] + len(level[i])
    dp[i][0] = dp[i-1][1]

print(deepestLevel)
print(edge)
print(level)
print(dp)

print(min(dp[deepestLevel][1], dp[deepestLevel][0]))
