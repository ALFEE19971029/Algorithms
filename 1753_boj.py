import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)

V,E = map(int,input().split())

K = int(input())

graph = [[] for _ in range(V+1)]

distance = [INF]*(V+1)

for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q,(0,start))
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(K)
for i in range(1,V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])