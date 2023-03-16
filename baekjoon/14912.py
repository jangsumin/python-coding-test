# 숫자 빈도수

n, d = map(int, input().split())

s = ''
for i in range(1, n + 1):
  s += str(i)

cnt = 0
for i in range(len(s)):
  if str(d) == s[i]:
    cnt += 1

print(cnt)