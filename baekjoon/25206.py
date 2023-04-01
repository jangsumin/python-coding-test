# 너의 평점은

dic = {
  'A+': 4.5,
  'A0': 4,
  'B+': 3.5,
  'B0': 3,
  'C+': 2.5,
  'C0': 2,
  'D+': 1.5,
  'D0': 1,
  'F': 0
}

total = 0
sum = 0
for _ in range(20):
  name, score, grade = map(str, input().split())
  if grade != 'P':
    total += float(score) * dic[grade]
    sum += float(score)
print(total / sum)