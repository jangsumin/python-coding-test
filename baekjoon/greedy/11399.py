# ATM

n = int(input())
p = list(map(int, input().split()))

p.sort()

time = 0
for i in range(len(p)):
    time += p[i] * (len(p) - i)

print(time)