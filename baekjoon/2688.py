# 줄어들지 않아

t = int(input())
for _ in range(t):
  n = int(input())

  dp = [[0] * 10 for _ in range(65)]
  for i in range(0, 10):
    dp[1][i] = 1
  
  for i in range(1, n + 1):
    for j in range(0, 10):
      for k in range(j, 10):
        dp[i][j] += dp[i - 1][k]
  
  print(sum(dp[n]))