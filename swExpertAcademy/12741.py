# 두 전구(D3)

tc = int(input())
answer = []
for t in range(1, tc + 1):
  a, b, c, d = map(int, input().split())
  time = dict()

  for i in range(a, b):
    if i not in time:
      time[i] = 1
    else:
      time[i] += 1
  
  for i in range(c, d):
    if i not in time:
      time[i] = 1
    else:
      time[i] += 1
  
  res = 0
  for current in time:
    if time[current] == 2:
      res += 1
  answer.append(res)

for t in range(1, tc + 1):
  print(f'#{t} {answer[t - 1]}')