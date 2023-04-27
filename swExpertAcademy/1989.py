# 초심자의 회문 검샤(D2)

tc = int(input())
for t in range(1, tc + 1):
  s_list = list(input())

  if ''.join(s_list) == ''.join(list(reversed(s_list))):
    print(f'#{t} 1')
  else:
    print(f'#{t} 0')