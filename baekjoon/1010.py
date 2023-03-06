# 다리 놓기

t = int(input())

def factorial(n):
  res = 1
  while n >= 1:
    res *= n
    n -= 1
  return res

for _ in range(t):
  n, m = map(int, input().split())
  print(factorial(m) // (factorial(n) * factorial(m - n)))