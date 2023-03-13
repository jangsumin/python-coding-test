# 막대기

x = int(input())
cnt = 0
initial = 64

while x != 0:
  if x < initial:
    initial = initial // 2
  else:
    x -= initial
    cnt += 1

print(cnt)