# 항구에 들어오는 배(D3)

tc = int(input())
for t in range(1, tc + 1):
    n = int(input())
    dates = []
    for _ in range(n):
        dates.append(int(input()))
    
    # 1일은 모든 배가 들어오는 날
    # 주기 기억하기
    saves = []
    for date in dates:
        if date != 1:
            saves.append(date - 1)
    
    cnt = len(saves)
    i = 0
    pop_list = []
    while True:
        if i == len(saves) - 1:
            break
        if i in pop_list:
            i += 1
            continue
        for j in range(i + 1, len(saves)):
            if saves[j] % saves[i] == 0 and j not in pop_list:
                pop_list.append(j)
        i += 1
    
    print(f'#{t} {len(saves) - len(pop_list)}')