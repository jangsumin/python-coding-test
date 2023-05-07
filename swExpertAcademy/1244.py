# 최대 상금(D3)

tc = int(input())

def change(numbers, cnt):
  global result

  temp = ''
  for number in numbers:
    temp += number
  
  if int(temp) in result[cnt]:
    return
  else:
    result[cnt].append(int(temp))
  
  if cnt == 0:
    return
  
  n = len(numbers)
  for i in range(n):
    for j in range(i + 1, n):
      numbers[i], numbers[j] = numbers[j], numbers[i]
      change(numbers, cnt - 1)
      numbers[i], numbers[j] = numbers[j], numbers[i]


for t in range(1, tc + 1):
  temp, cnt = input().split()
  num_list = list(temp)
  result = [[] for _ in range(int(cnt) + 1)]

  change(num_list, int(cnt))
  print('#{} {}'.format(t, max(result[0])))