# 몇개고?

t, s = map(int, input().split())

if t >= 12 and t <= 16:
  if s == 0:
    print(320)
  else:
    print(280)
else:
  print(280)