import sys
input = sys.stdin.readline

N = int(input())
card = list(map(int,input().split()))
M = int(input())
find = list(map(int,input().split()))

card.sort()

def binarySearch(findVal):
    start = 0
    end = N - 1
    while start <= end:
        midIdx = (start+end)//2
        if card[midIdx] == findVal:
            return 1
        elif card[midIdx] < findVal:
            start = midIdx+1
        elif card[midIdx] > findVal:
            end = midIdx - 1
    return 0

for i in range(M):
    print(binarySearch(find[i]))
    
    
    
