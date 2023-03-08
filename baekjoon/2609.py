# 최대공약수와 최소공배수

a, b = map(int, input().split())

i = 1
gcd = 0
lcd = 0

small = min(a, b)
while True:
  if a % small == 0 and b % small == 0:
    gcd = small
    break
  small -= 1

while True:
  if (a * i) % b == 0:
    lcd = a * i
    break
  i += 1

print(gcd)
print(lcd)