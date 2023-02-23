import sys
input = sys.stdin.readline

N, M = map(int,input().split())

diamond = [0] + [int(input()) for _ in range(N)]

sumArr = [0]*(N+1)

for i in range(1,N+1):
    sumArr[i] = sumArr[i-1] + diamond[i]





