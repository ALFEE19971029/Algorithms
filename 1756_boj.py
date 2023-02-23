d, n = map(int, input().split())
oven = list(map(int, input().split()))
doughs = list(map(int, input().split()))
 
for i in range(1, len(oven)):  # 이분탐색 적용을 위해 적절히 변경
    if oven[i] > oven[i-1]:
        oven[i] = oven[i-1]
 
 
piled_loc = 0  # 도우가 어디 쌓이는지
lp, rp = 0, len(oven)-1
for dough in doughs:
    is_piled = False  # False로 남으면 도우를 더 못쌓는다는 뜻
 
    while lp <= rp:
        mid = (lp+rp) // 2
        diameter = oven[mid]
        if diameter >= dough:
            lp = mid + 1
            piled_loc = mid
            is_piled = True
        else:
            rp = mid - 1
 
    if not is_piled:
        piled_loc = -1
        break
 
    lp = 0
    rp = piled_loc - 1  # 도우가 쌓이면 rp값 갱신 
 
 
if piled_loc == -1:
    print(0)
else:
    print(piled_loc+1)