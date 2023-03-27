# 팩토리얼 0의 개수

n = int(input())

if n == 0:
  print(0)
  exit(0)

res = 1
cnt = 0
for i in range(1, n + 1):
  res *= i
  while res % 10 == 0:
    res = res // 10
    cnt += 1

print(cnt)