import sys
input = sys.stdin.readline

N, M = map(int,input().split())
arr = [0] + [int(input()) for _ in range(N)]

sumArr = [0]*(N+1)
sumArr[1] = arr[1]

for i in range(2,N+1):
    sumArr[i] = sumArr[i-1] + arr[i]

dp = [[0]*(M+1) for _ in range(N+1)]

dp[1][1] = sumArr[1]

for i in range(2,N+1):
    dp[i][1] = max(dp[i-1][1], dp[i-1][1] + arr[i])

for i in range(3,N+1):
    for j in range(2,min(M,(i+1)//2)+1):
        notInclude = dp[i-1][j]
        kIsOne = 0
        kIsTwo = 0
        maxVal = -1e9
        for k in range(1,i+1):
            if k == 1:
                kIsOne = sumArr[N]
            elif k == 2:
                kIsTwo = sumArr[N] - arr[1]
            else:
                maxVal = max(maxVal,dp[k-2][j-1] + sumArr[N] - sumArr[k-1])
        dp[i][j] = max(notInclude,kIsOne,kIsTwo,maxVal)

print(dp[N][M])


