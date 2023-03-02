# 트럭 주차
# 구현

time = [0] * 101
a, b, c = map(int, input().split())
for _ in range(3):
  start, end = map(int, input().split())
  for i in range(start, end):
    time[i] += 1

pay = 0
for cnt in time:
  if cnt == 1:
    pay += a * 1
  if cnt == 2:
    pay += b * 2
  if cnt == 3:
    pay += c * 3

print(pay)