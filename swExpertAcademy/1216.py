# 회문2(D3)

def checkPalin(string):
    isPalin = True
    length = len(string)
    for i in range(0, len(string) // 2):
        if string[i] != string[length - 1 - i]:
            isPalin = False
    return isPalin

tc = 10
row_len = 100
for _ in range(1, tc + 1):
    res = -1
    t = int(input())
    graph = []
    for i in range(row_len):
        graph.append(list(input()))
    
    # 가로로 체크, 세로로 체크
    cnt = 0
    for i in range(row_len):
        for j in range(row_len):
            for k in range(1, row_len - j + 1):
                if checkPalin(''.join(graph[i][j : j + k])):
                    if len(graph[i][j : j + k]) > res:
                        res = len(graph[i][j : j + k])
    
    for i in range(row_len):
        for j in range(row_len):
            verti_str = ''
            for k in range(0, row_len - j):
                cnt += 1
                verti_str += graph[j + k][i]
                if checkPalin(verti_str):
                    if len(verti_str) > res:
                      res = len(verti_str)
    
    print(f'#{t} {res}')