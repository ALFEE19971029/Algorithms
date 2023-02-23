import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int,input().split())

degree = [0]*(N+1)
graph = [[] for _ in range(N+1)]
ans = []
queue = deque()

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    degree[b] += 1

for i in range(1,N+1):
    if degree[i] == 0:
        queue.append(i)

while queue:
    cur = queue.popleft()
    ans.append(cur)
    for i in graph[cur]:
        degree[i] -= 1
        if degree[i] == 0:
            queue.append(i)

for i in range(len(ans)):
    print(ans[i], end=" ")