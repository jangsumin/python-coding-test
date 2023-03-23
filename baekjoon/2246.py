# 콘도 선정

n = int(input())
condos = []
for _ in range(n):
  d, c = map(int, input().split())
  condos.append([c, d])

condos.sort()
result = 0
cost = 10001
for el in condos:
  temp = el[1]
  if temp < cost:
    cost = temp
    result += 1
print(result)