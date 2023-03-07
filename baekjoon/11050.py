# 이항 계수 1

n, k = map(int, input().split())

def factorial(n):
  res = 1
  while n >= 1:
    res *= n
    n -= 1
  return res

print(factorial(n) // (factorial(k) * factorial(n - k)))