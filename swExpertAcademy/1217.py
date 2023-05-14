# 거듭 제곱(D3)

def continuous_multiply(n, m):
    if m == 0:
        return 1
    else:
        return n * continuous_multiply(n, m - 1)

for _ in range(1, 11):
    t = int(input())
    n, m = map(int, input().split())

    res = continuous_multiply(n, m)
    print(f'#{t} {res}')
