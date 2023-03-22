# 접미사 배열

s = input()
arr = []
for i in range(0, len(s)):
  arr.append(s[i : len(s) + 1])

arr = sorted(arr)
for el in arr:
  print(el)