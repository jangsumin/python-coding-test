# 2xn 타일링

# 맞지만 메모리 초과
# from itertools import combinations

# n = int(input())
# cnt = 0

# for i in range(0, n // 2 + 1):
#   tiles = [1] * (n - (i * 2))
#   one_size_tiles = n - (i * 2)
#   tiles += [2] * i
#   cnt += len(list(combinations(tiles, one_size_tiles)))

# print(cnt % 10007)

n = int(input())
dp = [0, 1, 2]
for i in range(3, n + 1):
  dp.append((dp[i - 1] + dp[i - 2]) % 10007)
print(dp[n])