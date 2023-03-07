# 요세푸스 문제 0

n, k = map(int, input().split())

arr = [i for i in range(1, n + 1)]

res = list()
i = 1
while len(arr):
  if i % k != 0:
    arr.append(arr.pop(0))
  else:
    res.append(arr.pop(0))
  i += 1

print('<', end='')
print(', '.join(map(str, res)), end='')
print('>')