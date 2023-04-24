# 안테나

n = int(input())
location_list = list(map(int, input().split()))

location_list.sort()
if n % 2 == 0:
  sum1 = 0
  sum2 = 0
  for location in location_list:
    sum1 += abs(location - location_list[n // 2 - 1])
    sum2 += abs(location - location_list[n // 2])
  if sum1 == sum2:
    print(location_list[n // 2 - 1])
  elif sum1 > sum2:
    print(location_list[n // 2])
  else:
    print(location_list[n // 2 - 1])
else:
  print(location_list[n // 2])