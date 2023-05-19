# 승률 비교하기(D3)

tc = int(input())
res = []
for t in range(1, tc + 1):
    a, b, c, d = map(int, input().split())
    if a / b == c / d:
        res.append((t, 'DRAW'))
    if a / b > c / d:
        res.append((t, 'ALICE'))
    if a / b < c / d:
        res.append((t, 'BOB'))

for el in res:
    print(f'#{el[0]} {el[1]}')