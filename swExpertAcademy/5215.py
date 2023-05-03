# 햄버거 다이어트(D3)

# combinations 쓰면 답은 맞는데 Runtime Error 발생

tc = int(input())

def dfs(idx, cal, sco):
  global score, n, l

  # print(idx, sco, cal)

  for i in range(idx + 1, n):
    if cal + info[i][1] <= l:
      dfs(i, cal + info[i][1], sco + info[i][0])
    else:
      score = max(score, sco)
  
  # 마지막 인덱스에 대한 처리
  score = max(score, sco)
  
for t in range(1, tc + 1):
  n, l = map(int, input().split())
  info = [tuple(map(int, input().split())) for _ in range(n)]
  # print(info)
  
  score = 0

  for i in range(n):
    dfs(i, info[i][1], info[i][0])

  print('#%d %d' % (t, score))