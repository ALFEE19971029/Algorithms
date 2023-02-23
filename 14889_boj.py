import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
playerNum = [i for i in range(N)]

minVal = 999999

def findSum(teamArr):
    sum = 0
    for i in teamArr:
        for j in range(N):
            if j != i and j in teamArr:
                sum += arr[i][j]
    return sum

team2 = set()
for team1 in combinations(playerNum,N//2):
    for j in playerNum:
        if j not in team1:
            team2.add(j)
    minVal = min(minVal,abs(findSum(team1)-findSum(team2))) 
    team2.clear()
    

print(minVal)