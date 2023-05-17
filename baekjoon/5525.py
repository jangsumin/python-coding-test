# IOIOI

n = int(input())
m = int(input())
s = input()

# 50점짜리 코드
# to_find = ''
# length = 2 * n + 1
# for i in range(length):
#     if i % 2 == 0:
#         to_find += 'I'
#     else:
#         to_find += 'O'

# cnt = 0
# for i in range(0, m - length + 1):
#     if s[i : i + length] == to_find:
#         cnt += 1

# print(cnt)

answer, i, cnt = 0, 0, 0

while i < m - 1:
    if s[i : i + 3] == 'IOI':
        i += 2
        cnt += 1
        if cnt == n:
            answer += 1
            cnt -= 1
    else:
        i += 1
        cnt = 0

print(answer)