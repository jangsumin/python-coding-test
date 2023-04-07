# 도서관

n, m = map(int, input().split())
dists = list(map(int, input().split()))

minus = []
plus = []
for dist in dists:
  if dist < 0:
    minus.append(dist)
  else:
    plus.append(dist)

res = 0
minus.sort()
plus.sort(reverse=True)
aim = []
for i in range(len(minus)):
  if i % m == 0:
    aim.append(-minus[i])
for i in range(len(plus)):
  if i % m == 0:
    aim.append(plus[i])
aim.sort(reverse=True)
print(aim)
for i in range(len(aim)):
  if i == 0:
    res += aim[i]
  else:
    res += 2 * aim[i]

print(res)