# 백설 공주와 일곱 난쟁이

hobit = []
for _ in range(9):
  hobit.append(int(input()))

sum_nums = sum(hobit)
fake1 = 0
fake2 = 0
for i in range(0, 8):
  for j in range(i + 1, 9):
    if sum_nums - hobit[i] - hobit[j] == 100:
      fake1 = i
      fake2 = j

# pop(index) 연산을 사용해도 됨.
for i in range(9):
  if i != fake1 and i != fake2:
    print(hobit[i])