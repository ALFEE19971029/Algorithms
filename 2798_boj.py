N, M = map(int,input().split())
arr = list(map(int,input().split()))
ans = 0
diff = 0
min = 9999999
break1 = True
break2 = True

for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            sumVal = arr[i] + arr[j] + arr[k]
            diff = M - sumVal
            if  sumVal == M:
                break1 = False
                ans = sumVal
                break 
            elif sumVal < M and diff < min:
                min = diff
                ans = sumVal
            else:
                continue

        if break1 == False:
            break2 = False
            break
    if break2 == False:
        break

print(ans)