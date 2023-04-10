# 무한 문자열(D3)

tc = int(input())
# 최소공배수 구해서 그만큼 문자열 늘리고, 나중에 비교하기  
def lcm(x, y):
  max_len = max(len(x), len(y))
  while True:
    if max_len % len(x) == 0 and max_len % len(y) == 0:
      break
    max_len += 1
  return max_len

for i in range(1, tc + 1):
  s, t = map(str, input().split())
  new_s = s * (lcm(s, t) // len(s))
  new_t = t * (lcm(s, t) // len(t))
  if new_s == new_t:
    print(f'#{i} yes')
  else:
    print(f'#{i} no')