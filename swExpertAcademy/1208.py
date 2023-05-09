# Flatten(D3)

for t in range(1, 11):
  dmp_cnt = int(input())
  row = list(map(int, input().split()))

  # 정렬한 후에 가장 앞에 있는 것과 뒤에 있는 원소 +1, -1
  # 위 과정을 거치고 나서 가장 작거나 큰 원소가 안된다면 다시 정렬
  row.sort()
  i = 0
  while True:
    if i == dmp_cnt:
      break
    row[0] += 1
    row[-1] -= 1
    if row[0] != min(row) or row[-1] != max(row):
      row.sort()
    i += 1
  print(f'#{t} {max(row) - min(row)}')