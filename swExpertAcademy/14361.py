# 숫자가 같은 배수(D3)

tc = int(input())
for i in range(1, tc + 1):
  n = input()
  initial_len = len(n)
  j = 2
  isPossible = False
  while True:
    multiply = str(int(n) * j)
    #print(multiply)
    if len(multiply) > initial_len:
      break
    if sorted(list(multiply)) == sorted(list(n)):
      isPossible = True
      break
    j += 1

  if isPossible:
    print(f'#{i} possible')
  else:
    print(f'#{i} impossible')