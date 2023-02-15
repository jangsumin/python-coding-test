# 등수 매기기

import sys

n = int(sys.stdin.readline())

grade = []
for i in range(n):
    grade.append(int(sys.stdin.readline()))

grade.sort()

sum = 0
for i in range(1, len(grade) + 1):
    sum += abs(i - grade[i - 1])

print(sum)