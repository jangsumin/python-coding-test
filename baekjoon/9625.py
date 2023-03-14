# BABBA

k = int(input())
a = 1
b = 0

while k != 0:
  a, b = b, a + b
  k -= 1

print(str(a) + ' ' + str(b))