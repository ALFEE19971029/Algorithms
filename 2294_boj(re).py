import sys
input = sys.stdin.readline
n, k = map(int,input().split())
coins = [int(input()) for _ in range(n)]
minVal = 9999999999

dp = [9999999999] * (k+1)
dp[0] = 0

for i in range(1,k+1):
    for c in coins:
        if i - c >= 0 and minVal > dp[i-c]:
             minVal = dp[i-c]
    if minVal < 9999999999:
        dp[i] = minVal+1
    minVal = 9999999999

if dp[k] == 9999999999:
    print(-1)
else:
    print(dp[k])