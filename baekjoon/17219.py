# 비밀번호 찾기

n, m = map(int, input().split())

dic = {}
for _ in range(n):
  site, password = map(str, input().split())
  dic[site] = password

for _ in range(m):
  query = input()
  print(dic[query])