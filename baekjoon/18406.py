# 럭키 스트레이트

n = input()
length = len(n)
front, back = n[:(length // 2)], n[-(length // 2):]

if sum(list(map(int, front))) == sum(list(map(int, back))):
  print('LUCKY')
else:
  print('READY')