import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)

N,E = map(int,input().split())

graph = [[] for _ in range(N+1)]

for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

first, second = map(int,input().split())

def dijkstra(start,end):
    distance = [INF]*(N+1)
    distance[start] = 0
    q = []
    heapq.heappush(q,(0,start))
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:    
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    return distance[end]

ans1 = dijkstra(1,first) + dijkstra(first,second) + dijkstra(second, N)
ans2 = dijkstra(1,second) + dijkstra(second,first) + dijkstra(first, N)
if ans1 >= INF and ans2 >= INF:
    print(-1)
else:
    print(min(ans1,ans2))