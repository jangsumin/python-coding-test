# 퇴사 2

n = int(input())
dp = [0] * (n + 1)
info = []
for _ in range(n):
  t, p = map(int, input().split())
  info.append([t, p])

m = 0
for i in range(n):
  t, p = info[i]
  m = max(m, dp[i])
  if i + t > n:
    continue
  dp[i + t] = max(m + p, dp[i + t])

print(max(dp))