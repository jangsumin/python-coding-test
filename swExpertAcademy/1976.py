# 시각 덧셈(D2)

tc = int(input())
for t in range(1, tc + 1):
    times = list(map(int, input().split()))
    current = times[0] * 60 + times[1]
    add = times[2] * 60 + times[3]

    res = current + add
    hour = res // 60
    minute = res % 60
    if hour > 12:
        hour -= 12
    print(f'#{t} {hour} {minute}')