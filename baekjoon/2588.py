# 곱셈

num1 = int(input())
num2 = int(input())

result1 = num1 * (num2 % 10)
result2 = num1 * ((num2 % 100) // 10)
result3 = num1 * (num2 // 100)
result4 = result3 * 100 + result2 * 10 + result1

print(result1)
print(result2)
print(result3)
print(result4)