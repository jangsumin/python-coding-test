# 과제 안 내신 분...?

arr = []
for _ in range(28):
  arr.append(int(input()))

ans = []
for i in range(1, 31):
  if i not in arr:
    ans.append(i)

print(min(ans))
print(max(ans))