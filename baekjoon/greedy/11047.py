# 동전 0

n, k = map(int, input().split())
coin_type = []
for i in range(n):
    coin_type.append(int(input()))

coin_type.sort(reverse=True)

result = 0
for i in coin_type:
    result += k // i
    k %= i

print(result)