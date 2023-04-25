# 세가지 합 구하기(D3)

tc = int(input())
result = []
for t in range(1, tc + 1):
  n = int(input())
  s1 = n * (n + 1) // 2
  s2 = n ** 2
  s3 = n * (n + 1)
  
  print('#{} {} {} {}'.format(t, s1, s2, s3))