# 방 번호

string = list(input())

num = {
  '0': 0,
  '1': 0,
  '2': 0,
  '3': 0,
  '4': 0,
  '5': 0,
  '6': 0,
  '7': 0,
  '8': 0,
  '9': 0
}

for s in string:
  num[s] += 1

num['6'], num['9'] = (num['6'] + num['9']) // 2 + (num['6'] + num['9']) % 2, (num['6'] + num['9']) // 2  + (num['6'] + num['9']) % 2
res = max(num.values())
print(res)