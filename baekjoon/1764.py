# 듣보잡

n, m = map(int, input().split())

name = {}
for _ in range(n + m):
  s = str(input())
  if s in name:
    name[s] += 1
  else:
    name[s] = 1

cnt = 0
res = []
for key in name:
  if name[key] >= 2:
    cnt += 1
    res.append(key)
res = sorted(res)
print(cnt)
for el in res:
  print(el)