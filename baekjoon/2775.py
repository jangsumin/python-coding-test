# 부녀회장이 될테야

t = int(input())

for _ in range(t):
  k = int(input())
  n = int(input())

  a = 1
  b = 1
  for i in range(k + 1):
    a *= (n + i)
    b *= i + 1
  c = a // b
  
  print(c)