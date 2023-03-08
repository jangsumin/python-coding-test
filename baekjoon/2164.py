# 카드2

import math
n = int(input())

arr = [(i + 1) for i in range(n)]

# 시간 초과
# while len(arr) > 1:
#   arr.pop(0)
#   arr.append(arr.pop(0))

# print(arr[0])

obj = {}

temp = n
cnt = 0
while temp != 1:
  temp = temp // 2
  cnt += 1

start = 2 ** (cnt)
end =  2 ** (cnt + 1)

j = 2
for i in range(start, end + 1):
  if i == start:
    obj[i] = start
  else:
    obj[i] = j
    j += 2 

print(obj[n])