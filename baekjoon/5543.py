# 상근날드

money_list = list()
for _ in range(5):
  money_list.append(int(input()))

print(min(money_list[0], money_list[1], money_list[2]) + min(money_list[3], money_list[4]) - 50)