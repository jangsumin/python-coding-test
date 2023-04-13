 # 패션왕 신해빈

from itertools import combinations
t = int(input())
for _ in range(t):
  n = int(input())
  clothes_dict = {}
  for i in range(n):
    name, kind = map(str, input().split())
    if kind in clothes_dict.keys():
      clothes_dict[kind] += 1
    else:
      clothes_dict[kind] = 1
  
  cnt = 1
  for key in clothes_dict:
    cnt *= clothes_dict[key] + 1
  print(cnt - 1)