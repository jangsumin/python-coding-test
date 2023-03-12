# 스택 수열

n = int(input())

# arr = [i for i in range(1, n + 1)]
arr = []
result = []
cur = 1
isPrint = True
for i in range(n):
  num = int(input())
  while cur <= num:
    arr.append(cur)
    result.append('+')
    cur += 1

  if arr[-1] == num:
    arr.pop()
    result.append('-')
  else:
    print('NO')
    isPrint = False
    break

if isPrint:
  for i in result:
    print(i)