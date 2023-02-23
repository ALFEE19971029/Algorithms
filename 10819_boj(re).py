import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
maxVal = 0
track = []
visited = [False] * N
sum = 0

def backtracking(depth):
    global maxVal, sum
    if depth == N:
        for i in range(N-1):
            sum += abs(track[i] - track[i+1])
        maxVal = max(maxVal,sum)
        sum = 0
        return
    for i in range(N):
        if visited[i]:
            continue
        track.append(arr[i])
        visited[i] = True
        backtracking(depth+1)
        visited[i] = False
        track.pop()

backtracking(0)
print(maxVal)

# from itertools import permutations
# N = int(input())
# arr = list(map(int,input().split()))
# max = 0
# cnt = 0

# for per in permutations(arr):
#     for i in range(N-1):
#         cnt += abs(per[i] - per[i+1])
#         if cnt > max:
#             max = cnt
#     cnt = 0
# print(max)

