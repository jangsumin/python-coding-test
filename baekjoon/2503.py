# 숫자 야구
# 완전 탐색

from itertools import permutations

result = 0
n = int(input())
infos = []
for _ in range(n):
  infos.append(input())

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
combi = list(permutations(nums, 3))

baseball_nums = []
for tuple in combi:
  s = ''
  for i in tuple:
    s += str(i)
  baseball_nums.append(int(s))

for i in baseball_nums:
  correct_cnt = 0
  for info in infos:
    query, strike, ball = map(int, info.split())
    strike_answer = 0
    ball_answer = 0
    for j in range(0, 3):
      if str(i)[j] == str(query)[j]:
        strike_answer += 1
      elif str(i)[j] in list(str(query)):
        ball_answer += 1
    # print(strike_answer, ball_answer, end=' ')
    # print()
    if strike_answer != strike or ball_answer != ball:
      break
    else:
      correct_cnt += 1
  if correct_cnt == n:
    result += 1
  
print(result)