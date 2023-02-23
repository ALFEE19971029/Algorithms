import sys
input = sys.stdin.readline

N = int(input())

dpZero = [0]*(N+1)
dpOne = [0]*(N+1)

if N >= 1:
    dpZero[1] = 0
    dpOne[1] = 1
if N >= 2:
    dpZero[2] = 1
    dpOne[2] = 0

if N >= 3:
    for i in range(3,N+1):
        dpZero[i] = dpZero[i-1] + dpOne[i-1]
        dpOne[i] = dpZero[i-1]

print(dpZero[N] + dpOne[N])
