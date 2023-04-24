# 먹을 것인가 먹힐 것인가

t = int(input())
for _ in range(t):
  a, b = map(int, input().split())
  a_list = list(map(int, input().split()))
  b_list = list(map(int, input().split()))

  cnt = 0
  # 시간 초과 코드
  # for a in a_list:
  #   for b in b_list:
  #     if a > b:
  #       cnt += 1
  
  a_list.sort(reverse=True)
  b_list.sort(reverse=True)
  i, j = 0, 0
  while True:
    if j >= b:
      i += 1
      j = 0
    if i >= a:
      break

    if a_list[i] > b_list[j]:
      cnt += b - j
      j = 0
      i += 1
    else:
      j += 1

  print(cnt)