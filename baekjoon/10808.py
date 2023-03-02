# 알파벳 개수
# 문자열

s = input()
lst = [0] * 26
for i in s:
    lst[ord(i) - 97] += 1
for i in lst: 
    print(i, end= ' ')