# UCPC는 무엇의 약자일까?

s = list(input())

word = ''
for el in s:
  if el == 'U' and word == '':
    word = 'U'
  if el == 'C' and word == 'U':
    word = 'UC'
  if el == 'P' and word == 'UC':
    word = 'UCP'
  if el == 'C' and word == 'UCP':
    word = 'UCPC'

if word == 'UCPC':
  print('I love UCPC')
else:
  print('I hate UCPC')