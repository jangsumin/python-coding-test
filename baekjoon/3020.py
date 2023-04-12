# 개똥벌레

# n은 길이, h은 높이
n, h = map(int, input().split())

cnt = n
range_cnt = 0

bottom = [0] * (h + 1)
top = [0] * (h + 1)
for i in range(n):
  length = int(input())
  if i % 2 == 0:
      bottom[length] += 1
  else:
      top[length] += 1

result = [0] * h
for i in range(h - 1, 0, -1):
  bottom[i] += bottom[i + 1]
  top[i] += top[i + 1]

for i in range(1, h + 1):
  if cnt > (bottom[i] + top[h - i + 1]):
    cnt = bottom[i] + top[h - i + 1]
    range_cnt = 1
  elif cnt == (bottom[i] + top[h - i + 1]):
    range_cnt += 1

print(cnt, range_cnt)

# obs 배열 내에 짝수 인덱스에 있는 것들은 석순, 홀수는 종유석

# 시간 초과
# for i in range(n):
#   if i % 2 == 0:
#     for j in range(obs[i]):
#       range_h[j] += 1
#   else:
#     for j in range(obs[i]):
#       range_h[h - 1 - j] += 1