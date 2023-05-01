# 회문1(D3)

for t in range(1, 11):
  n = int(input())

  graph = []
  for _ in range(8):
    graph.append(list(input()))
  
  graph1 = [[row[i] for row in graph] for i in range(8)]

  cnt = 0
  for i in range(8):
    for j in range(0, 8 - n + 1):
      s = graph[i][j : j + n]
      s1 = graph1[i][j : j + n]

      isTrue = True
      isTrue1 = True
      for k in range(n // 2):
        if s[k] != s[n - k - 1]:
          isTrue = False
        if s1[k] != s1[n - k - 1]:
          isTrue1 = False
    
      if isTrue:
        # print(s)
        cnt += 1
      if isTrue1:
        cnt += 1
  
  print(f'#{t} {cnt}')