# 파도반 수열

t = int(input())

# 시간 초과
# def sol(n):
#   if n == 1:
#     return 1
#   elif n == 2:
#     return 1
#   elif n == 3:
#     return 1
#   else:
#     return sol(n - 2) + sol(n - 3)

arr = [1, 1, 1]
i = 4

for _ in range(t):
  n = int(input())
  if n <= 3:
    print(arr[n - 1])
  else:
    while i <= n:
      arr.append(arr[i - 4] + arr[i - 3])
      i += 1
    print(arr[n - 1])