# 교환학생(D3)

tc = int(input())
for t in range(1, tc + 1):
  n = int(input())
  # 일월화수목금토 순
  classes = list(map(int, input().split()))

  res = []
  for i in range(7):
    idx = i
    day_cnt = 0
    class_cnt = 0
    while True:
      if class_cnt == n:
        break

      if idx >= 7:
        idx %= 7
      if classes[idx] == 1:
        class_cnt += 1
      day_cnt += 1
      idx += 1
    res.append(day_cnt)
  print(f'#{t} {min(res)}')