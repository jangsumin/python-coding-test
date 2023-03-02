# 알바생 강호
# 그리디

import sys
input = sys.stdin.readline

n = int(input())
sum = 0
tips = []
for _ in range(n):
  tips.append(int(input()))

tips = sorted(tips, reverse=True)
for i in range(n):
  if tips[i] - i < 0:
    sum += 0
  else: 
    sum += tips[i] - i
print(sum)