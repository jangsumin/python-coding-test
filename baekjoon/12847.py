# 꿀 아르바이트

n, m = map(int, input().split())
pay = list(map(int, input().split()))

# 시간초과 코드
# profit = []
# for i in range(0, n - m + 1):
#   sum = 0
#   for j in range(i, i + m):
#     sum += pay[j]
#   profit.append(sum)
# print(max(profit))

sum = 0
# 맨 앞 m개의 합 구하기
for i in range(m):
  sum += pay[i]

start = 0
end = m
max_sum = sum
while end < n:
  # 앞에 빼고 뒤에 더해서 새로운 누적합 계산
  sum = sum + pay[end] - pay[start]
  max_sum = max(max_sum, sum)
  start += 1
  end += 1
print(max_sum)