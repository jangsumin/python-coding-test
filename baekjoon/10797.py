# 10부제

n = input()
arr = list(map(int, input().split()))

ans = 0
for el in arr:
  if str(el)[-1] == n:
    ans += 1
print(ans)