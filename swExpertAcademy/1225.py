# 암호생성기(D3)

for _ in range(10):
    t = int(input())
    num_list = list(map(int, input().split()))

    decrease = 1
    while True:
        if decrease >= 6:
            decrease = 1
        picked_num = num_list.pop(0)
        if picked_num - decrease <= 0:
            num_list.append(0)
            break
        num_list.append(picked_num - decrease)
        decrease += 1
    
    print(f'#{t}', end=' ')
    for num in num_list:
        print(num, end=' ')
    print()