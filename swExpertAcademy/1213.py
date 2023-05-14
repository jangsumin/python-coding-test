# String(D3)

for _ in range(1, 11):
    t = int(input())
    to_find = input()
    s = input()

    cnt = 0
    for i in range(len(s) - len(to_find) + 1):
        isRight = True
        for j in range(len(to_find)):
            if s[i + j] != to_find[j]:
                isRight = False
                break
        if isRight:
            cnt += 1
    print(f'#{t} {cnt}')
