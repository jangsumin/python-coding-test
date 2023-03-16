# 개수 세기

n = int(input())
arr = list(map(int, input().split()))
to_find = int(input())

cnt = 0
for el in arr:
  if el == to_find:
    cnt += 1
print(cnt)