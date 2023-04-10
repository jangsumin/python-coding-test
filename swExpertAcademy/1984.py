# 중간 평균값 구하기(D2)

tc = int(input())
for i in range(1, tc + 1):
  arr = list(map(int, input().split()))
  print(f'#{i} {round((sum(arr) - max(arr) - min(arr)) / 8)}')