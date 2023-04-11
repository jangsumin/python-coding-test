# 보충학습과 평균(D3)

tc = int(input())
for t in range(1, tc + 1):
  scores = list(map(int, input().split()))

  sum = 0
  for score in scores:
    if score < 40:
      sum += 40
    else:
      sum += score
  print(f'#{t} {sum // 5}')