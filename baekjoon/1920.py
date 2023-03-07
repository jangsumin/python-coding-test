# 수 찾기

import sys
input = sys.stdin.readline

n = int(input())
target = set(map(int, input().split()))
m = int(input())
source = list(map(int, input().split()))

for num in source:
  print(1) if num in target else print(0)