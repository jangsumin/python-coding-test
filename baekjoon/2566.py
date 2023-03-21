# 최댓값

doubled_arr = [] 
for _ in range(9):
  doubled_arr.append(list(map(int, input().split())))

max_num = max(map(max, doubled_arr))
for i in range(9):
  for j in range(9):
    if doubled_arr[i][j] == max_num:
      print(max_num)
      print(i + 1, j + 1)
      exit(0)