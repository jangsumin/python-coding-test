# 근손실

n, k = map(int, input().split())
gains = list(map(int, input().split()))

from itertools import permutations
arr = [i for i in range(1, n + 1)]

cnt = 0
for permutation in list(permutations(arr)):
  muscle = 500
  success = True
  for i in range(len(permutation)):
    muscle += gains[list(permutation)[i] - 1] - k
    if muscle < 500:
      success = False
      break
  if success == True:
    cnt += 1

print(cnt)