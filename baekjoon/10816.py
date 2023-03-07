# 숫자 카드 2

n = int(input())
target = list(map(int, input().split()))
m = int(input())
source = list(map(int, input().split()))

obj = {}
for i in range(n):
  if target[i] in obj:
    obj[target[i]] += 1
  else:
    obj[target[i]] = 1

# print(obj)

res = [0 for _ in range(m)]
for i in range(m):
  if source[i] in obj:
    res[i] = obj[source[i]]
  else:
    res[i] = 0

print(' '.join(list(map(str, res))))