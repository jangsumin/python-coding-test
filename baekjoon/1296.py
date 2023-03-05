# 팀 이름 정하기

name = input()
n = int(input())
team_name = []
for _ in range(n):
  team_name.append(input())

possibility = {}
for i in range(n):
  concat_name = name + team_name[i]
  l = len(concat_name) - len(concat_name.replace('L', ''))
  o = len(concat_name) - len(concat_name.replace('O', ''))
  v = len(concat_name) - len(concat_name.replace('V', ''))
  e = len(concat_name) - len(concat_name.replace('E', ''))
  possibility[team_name[i]] = ((l + o) * (l + v) * (l + e) * (o + v) * (o + e) * (v + e)) % 100

possibility = list(possibility.items())
possibility.sort(key=lambda x: x[0])
possibility.sort(key=lambda x: x[1], reverse=True)
print(possibility[0][0])