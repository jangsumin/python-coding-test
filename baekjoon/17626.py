# Four Squares

n = int(input())

# 그리디 형식으로 풀면 틀림
# i = 1
# cnt = 0
# while True:
#   if n == 0:
#     break

#   while i * i <= n:
#     i += 1
#   i -= 1
#   print(i)
#   n -= i * i
#   cnt += 1
#   i = 1

# print(cnt)

dp = [0, 1]
for i in range(2, n + 1):
  min_value = 1e9
  j = 1

  while j ** 2 <= i:
    min_value = min(min_value, dp[i - j ** 2])
    j += 1
  
  dp.append(min_value + 1)
print(dp[n])