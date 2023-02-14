# 거스름돈

pay = int(input())
rest = 1000 - pay

answer = (rest // 500) + (rest % 500) // 100 + (rest % 100) // 50 + (rest % 50) // 10 + (rest  % 10) // 5 + (rest % 5) // 1
print(answer)