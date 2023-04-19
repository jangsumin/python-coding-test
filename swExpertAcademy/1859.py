# 백만 장자 프로젝트(D2)

t = int(input())
for i in range(1, t + 1):
  n = int(input())
  cost_list = list(map(int, input().split()))

  profit = 0
  max_val = cost_list[-1]
  
  for j in range(n - 1, -1, -1):
    if cost_list[j] >= max_val:
      max_val = cost_list[j]
    profit += max_val - cost_list[j]
  
  print(f'#{i} {profit}')

# 틀린 코드

# t = int(input())
# for i in range(1, t + 1):
#   n = int(input())
#   cost_list = list(map(int, input().split()))

#   profit = 0
#   cnt = 0
#   copy = sorted(cost_list)
  
#   for j in range(n):
#     if cost_list[j] == copy[-1]:
#       profit += cnt * cost_list[j]
#       cnt = 0
#       copy.pop()
#     else:
#       profit -= cost_list[j]
#       cnt += 1
  
#   print(f'#{i} {profit}')