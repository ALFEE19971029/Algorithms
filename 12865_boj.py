import sys
input = sys.stdin.readline

N, K = map(int,input().split())

things = []

for _ in range(N):
    w, v = map(int,input().split())
    things.append((w,v))

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(N+1):
    for j in range(K+1):
        if i == 0 or j == 0:
            dp[i][j] = 0
        else:
            if things[i-1][0] <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-things[i-1][0]] + things[i-1][1])
            else:
                dp[i][j] = dp[i-1][j]

print(dp[N][K])