# 팩토리얼5

n = int(input())

res = 1
i = 2
while i <= n:
  res *= i
  i += 1
  # if res % 10 == 0:
  #   res = res // 10
  while True:
    if str(res)[-1] == "0":
      res = res // 10
    else:
      break
  res %= 10000000000000

print(str(res)[-5 : ])