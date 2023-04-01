# 최소공배수

a, b = map(int, input().split())

max_num = max(a, b)
initial_num = max(a, b)
i = 2
while True:
  if max_num % a == 0 and max_num % b == 0:
    print(max_num)
    break
  max_num = initial_num * i
  i += 1