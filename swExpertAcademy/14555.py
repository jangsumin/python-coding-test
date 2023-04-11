# 공과 잡초(D3)

tc = int(input())
for t in range(1, tc + 1):
  land = list(input())

  cnt = 0
  # .은 넘어가고 |이 공의 일부가 될 수 있을지 확인하기만 하면 됨
  for i in range(0, len(land) - 1):
    if land[i] == '(' and land[i + 1] == '|':
      cnt += 1
    elif land[i] == '|' and land[i + 1] == ')':
      cnt += 1
    elif land[i] == '(' and land[i + 1] == ')':
      cnt += 1
    else:
      continue
  print(f'#{t} {cnt}')