# 교수가 된 현우

# import math
t = int(input())
for _ in range(t):
  n = int(input())
  
  # print(math.factorial(n))
  value = 1
  five_cnt = 0
  i = 5
  while i <= n:
    # 2와 5로 얼마나 나눠 떨어지는지 확인해서 카운트 증가
    # 하지만 5의 인수가 훨씬 적으므로 5에 대해서만 고려
    five_cnt += n // i
    i *= 5
  
  print(five_cnt)