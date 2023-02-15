# 잃어버린 괄호

numbers = list(map(str, input().split('-')))

result = 0

for i in range(len(numbers)):
    sum_numbers = list(map(int, numbers[i].split('+')))
    sum = 0
    for j in sum_numbers:
        sum += j
    if i == 0:
        result += sum
    else:    
        result -= sum

print(result)