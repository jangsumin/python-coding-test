# 소수의 연속합

n = int(input())

a = [False, False] + [True] * (n - 1)
prime_num = list()

for i in range(2, n + 1):
  # 에라토스테네스의 체
  if a[i]:
    prime_num.append(i)
    for j in range(2 * i, n + 1, i):
      a[j] = False

ans = 0
start = 0
end = 0
while end <= len(prime_num):
  temp_sum = sum(prime_num[start:end])
  if temp_sum == n:
    ans += 1
    end += 1
  elif temp_sum < n:
    end += 1
  else:
    start += 1

print(ans)