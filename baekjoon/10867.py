# 중복 빼고 정렬하기

n = int(input())
arr = list(map(int, input().split()))

arr = sorted(set(arr))
for el in arr:
  print(el, end=' ')