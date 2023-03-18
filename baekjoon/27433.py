# 팩토리얼 2

def factorial(n):
  res = 1
  if n == 0:
    return res
  while n != 1:
    res *= n
    n -= 1
  return res

if __name__ == '__main__':
  n = int(input())
  print(factorial(n))