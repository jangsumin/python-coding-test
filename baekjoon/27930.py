# 당신은 운명을 믿나요?

s = list(input())

korea = ['K', 'O', 'R', 'E', 'A']
yonsei = ['Y', 'O', 'N', 'S', 'E', 'I']

i, k, y = 0, 0, 0
while i <= len(s) - 1:
  if s[i] == korea[k]:
    k += 1
  if s[i] == yonsei[y]:
    y += 1
  if k == 5:
    print('KOREA')
    break
  if y == 6:
    print('YONSEI')
    break
  i += 1