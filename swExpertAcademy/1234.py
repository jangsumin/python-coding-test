# 비밀번호(D3)

for t in range(1, 11):
    length, string = input().split()
    length = int(length)
    string = list(string)

    while True:
        length = len(string)
        change_cnt = 0
        for i in range(length - 1):
            if string[i] == 'X':
                continue
            if string[i] == string[i + 1]:
                change_cnt += 1
                string[i] = 'X'
                string[i + 1] = 'X'
        
        if change_cnt == 0:
            break
        
        string = ''.join(string).replace('X', '')
        string = list(string) 

        # print(string)

    string = ''.join(string)
    print(f'#{t} {string}')