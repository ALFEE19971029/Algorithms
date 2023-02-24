import sys
import heapq
input = sys.stdin.readline

N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]
INF = float("INF")
distanceFox = [INF]*(N+1)
distanceWolf = [INF]*(N+1)

for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def fox(start):
    q = []
    heapq.heappush(q,(0,start))
    distanceFox[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if dist > distanceFox[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distanceFox[i[0]]:
                distanceFox[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

def wolf(start):
    q = []
    heapq.heappush(q,(0,start,True))
    distanceWolf[start] = 0
    cnt = 0
    while q:
        dist,now,fast = heapq.heappop(q)
        if dist > distanceWolf[now]:
            continue
        for i in graph[now]:
            if fast == True:
                cost = dist + i[1]/2
                fast = False
            else:
                cost = dist + i[1]*2
                fast = True
            if cost < distanceWolf[i[0]]:
                distanceWolf[i[0]] = cost
                heapq.heappush(q,(cost,i[0],fast))

fox(1)
wolf(1)
print(distanceFox)
print(distanceWolf)

count = 0
for i in range(1,N+1):
    if distanceFox[i] < distanceWolf[i]:
        count += 1

print(count)