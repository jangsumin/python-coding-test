# 일곱 난쟁이

height = []
for _ in range(9):
  height.append(int(input()))

to_find = sum(height) - 100
save1, save2 = 0, 0
for i in range(0, 8):
  for j in range(i + 1, 9):
    if height[i] + height[j] == to_find:
      save1 = height[i]
      save2 = height[j]

height.sort()
for el in height:
  if el == save1 or el == save2:
    continue
  print(el)