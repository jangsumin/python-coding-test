# 합(D3)

tc = int(input())
for t in range(1, tc + 1):
    n = int(input())
    num_list = list(map(int, input().split()))

    sum_list = [0] * len(num_list)
    sum_list[0] = num_list[0]

    for i in range(1, len(sum_list)):
        sum_list[i] = max(0, sum_list[i - 1]) + num_list[i]
    print(f'#{t} {max(sum_list)}')