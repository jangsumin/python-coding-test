# 부분수열의 합

n, s = map(int, input().split())
num_list = list(map(int, input().split()))

cnt = 0

def subset(idx, sub_sum):
  global cnt
  if idx >= n:
    return
  sub_sum += num_list[idx]
  if sub_sum == s:
    cnt += 1
  subset(idx + 1, sub_sum)
  subset(idx + 1, sub_sum - num_list[idx])

subset(0, 0)
print(cnt)