# 분수 합

import math

numerator1, devider1 = map(int, input().split())
numerator2, devider2 = map(int, input().split())

res2 = math.lcm(devider1, devider2)
res1 = res2 // devider1 * numerator1 + res2 // devider2 * numerator2

print(res1 // math.gcd(res1, res2), end = ' ')
print(res2 // math.gcd(res1, res2))