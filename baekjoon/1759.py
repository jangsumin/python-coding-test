# 암호 만들기

l, c = map(int, input().split())
arr = list(map(str, input().split()))

arr.sort()
vowel = ['a', 'e', 'i', 'o', 'u']

def backtracking(idx, s, vc, cc):
  if idx >= c:
    return

  if arr[idx] in vowel:
    vc += 1
  else:
    cc += 1

  s += arr[idx]

  if len(s) == l and vc >= 1 and cc >= 2:
    print(s)
  
  backtracking(idx + 1, s, vc, cc)
  if arr[idx] in vowel:
    backtracking(idx + 1, s[0 : -1], vc - 1, cc)
  else:
    backtracking(idx + 1, s[0 : -1], vc, cc - 1)

backtracking(0, '', 0, 0)