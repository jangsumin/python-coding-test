# 외로운 문자(D3)

tc = int(input())
for t in range(1, tc + 1):
  dic = dict()
  s = input()
  for alphabet in s:
    if alphabet not in dic:
      dic[alphabet] = 1
    else:
      dic[alphabet] += 1
  
  result = []
  for key in dic:
    if dic[key] % 2 == 1:
      result.append(key)
  result.sort()

  ans = ''.join(result)
  if len(result) == 0:
    print(f'#{t} Good')
  else:
    print(f'#{t} {ans}')