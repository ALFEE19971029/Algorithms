import sys
from itertools import permutations
input = sys.stdin.readline
N = int(input())
arr = list(map(int,input().split()))

addCnt, subCnt, multCnt, divCnt = map(int,(input().split()))

minVal = 1000000001
maxVal = -1000000001

def myAdd(a,b):
    if a < 0:
        return -(-a//b)
    return a // b

operArr = [1]*addCnt + [2]*subCnt + [3]*multCnt + [4]*divCnt

temp = arr[0]

for operands in permutations(operArr):
    for i in range(N-1):
        if operands[i] == 1:
            temp += arr[i+1]
        elif operands[i] == 2:
            temp -= arr[i+1]
        elif operands[i] == 3:
            temp *= arr[i+1]
        else:
            temp = myAdd(temp,arr[i+1])
    maxVal = max(maxVal, temp)
    minVal = min(minVal,temp)
    temp = arr[0]

print(maxVal)
print(minVal)
    
