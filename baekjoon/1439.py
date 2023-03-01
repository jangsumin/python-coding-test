# 뒤집기

string = input()
zero = string.split('1')
one = string.split('0') 

zero_cnt = 0
one_cnt = 0
for i in zero:
    if i != '':
        zero_cnt += 1
for i in one:
    if i != '':
        one_cnt += 1

print(min(zero_cnt, one_cnt))