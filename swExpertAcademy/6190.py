# 정곤이의 단조 증가하는 수(D3)

from itertools import combinations
tc = int(input())

def is_increasing_number(num):
  check = True
  string = str(num)
  for i in range(0, len(string) - 1):
    if string[i] > string[i + 1]:
      check = False
      break
  return check

for t in range(1, tc + 1):
  n = int(input())
  num_list = list(map(int, input().split()))
  res = []

  for combi in combinations(range(1, n + 1), 2):
    new_num = num_list[combi[0] - 1] * num_list[combi[1] - 1]
    if is_increasing_number(new_num):
      res.append(new_num)
  
  if len(res) == 0:
    print(f'#{t} -1')
  else:
    print(f'#{t} {max(res)}')