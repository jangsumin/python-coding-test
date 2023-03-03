# 감소하는 수

# 입력
import sys
x = int(sys.stdin.readline())

from itertools import combinations

group = []
for i in range(1, 11):
  for combi in list(combinations(range(0, 10), i)):
    num = ''.join(map(str, reversed(list(combi))))
    group.append(int(num))

group.sort()

# 총 길이는 1023
try:
  print(group[x])
except:
  print(-1)

# 아래처럼 풀면 시간 초과
# index = 0
# num = 0
# group = []
# while index <= x:
#   if x > 9876543210:
#     print(-1)
#     break
#   if list(str(num)) == sorted(list(str(num)), reverse=True) and len(list(str(num))) == len(set(list(str(num)))):
#     index += 1
#     group.append(num)
#   num += 1

# print(num - 1)