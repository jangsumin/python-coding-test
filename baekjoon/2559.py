# 수열

n, k = map(int, input().split())
temps = list(map(int, input().split()))

result = []
initial = 0
for i in range(k):
  initial += temps[i]
result.append(initial)

for i in range(n - k):
  result.append(result[-1] - temps[i] + temps[k + i])

print(max(result))