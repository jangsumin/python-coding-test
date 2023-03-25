# 나는야 포켓몬 마스터 이다솜

import sys
input = sys.stdin.readline
n, m = map(int, input().split())

arr = dict()
for i in range(1, n + 1):
  pokemon = input().rstrip()
  arr[i] = pokemon
  arr[pokemon] = i

for i in range(m):
  question = input().rstrip()
  if question.isdigit():
    print(arr[int(question)])
  else:
    print(arr[question])