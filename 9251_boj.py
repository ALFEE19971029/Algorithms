import sys
input = sys.stdin.readline

first = list(input().strip())
second = list(input().strip())

dp = [[0 for _ in range(len(second)+1)] for _ in range(len(first)+1)]

for i in range(len(first)+1):
    for j in range(len(second)+1):
        if i == 0 or j == 0:
            dp[i][j] = 0
        else:
            if first[i-1] == second[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(first)][len(second)])