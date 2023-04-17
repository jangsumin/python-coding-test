# 두 개의 숫자열(D2)

tc = int(input())
for i in range(1, tc + 1):
  n, m = map(int, input().split())
  n_list = list(map(int, input().split()))
  m_list = list(map(int, input().split()))

  result = []
  if n >= m:
    for j in range(0, n - m + 1):
      sum = 0
      for k in range(0, m):
        sum += n_list[j + k] * m_list[k]
      result.append(sum)
  else:
    for j in range(0, m - n + 1):
      sum = 0
      for k in range(0, n):
        sum += n_list[k] * m_list[j + k]
      result.append(sum)
  print(f'#{i} {max(result)}')