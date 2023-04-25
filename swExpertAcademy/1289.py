# 원재의 메모리 복구하기(D3)

tc = int(input())
for t in range(1, tc + 1):
  memory = list(map(int, input()))

  initial = [0] * len(memory)
  change_cnt = 0
  ans = 0
  for i in range(len(memory)):
    if change_cnt % 2 == 1:
      if memory[i] == 1:
        memory[i] = 0
      else:
        memory[i] = 1

    if memory[i] != initial[i]:
      ans += 1
      change_cnt += 1
  
  print(f'#{t} {ans}')