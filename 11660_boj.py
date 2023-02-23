import sys
input = sys.stdin.readline

N, M = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]
accumulate = [[0]*(N+1) for _ in range(N+1)]

for x in range(N):
    for y in range(N):
        accumulate[x+1][y+1] = arr[x][y] + accumulate[x][y+1] + accumulate[x+1][y] - accumulate[x][y]

for _ in range(M):
    x1,y1,x2,y2 = map(int,input().split())
    print(accumulate[x2][y2] + accumulate[x1-1][y1-1] - accumulate[x1-1][y2] - accumulate[x2][y1-1])
