import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int,input().split())
arr = [list(map(int,input().rstrip())) for _ in range(N)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y,depth):
    queue = deque()
    queue.append((x,y,depth))
    while queue:
        ox, oy, temp = queue.popleft()
        for i in range(4):
            nx = ox + dx[i]
            ny = oy + dy[i]
            if nx == N-1 and ny == M-1:
                return temp+1
            if 0<=nx<=N-1 and 0<=ny<=M-1 and arr[nx][ny] == 1:
                queue.append((nx,ny,temp+1))
                arr[nx][ny] = 0

print(bfs(0,0,1))
