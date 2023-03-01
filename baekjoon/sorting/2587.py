# 대표값2

num_list = []
for i in range(5):
  num = int(input())
  num_list.append(num)

print(round(sum(num_list) / 5))
print(sorted(num_list)[2])