# View(D3)

for t in range(1, 11):
  n = int(input())
  buildings = list(map(int, input().split()))

  cnt = 0
  for i in range(2, n - 2):
    arround = [buildings[i - 2], buildings[i - 1], buildings[i + 1], buildings[i + 2]]
    isViewGood = True
    for building in arround:
      if building >= buildings[i]:
        isViewGood = False
        break
  
    if isViewGood:
      cnt += buildings[i] - max(arround)
  
  print(f'#{t} {cnt}')