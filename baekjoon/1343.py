# 폴리오미노

s = input().split('.')

ans = ''
for group in s:
  if len(group) % 2 == 1:
    print(-1)
    exit(0) 
  else:
    ans += 'AAAA' * (len(group) // 4)
    if len(group) % 4 == 2:
      ans += 'BB'
  ans += '.'

print(ans[0 : -1])