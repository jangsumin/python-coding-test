# 정사각형 판정(D3)

tc = int(input())
for t in range(1, tc + 1):
    n = int(input())
    graph = [list(input()) for _ in range(n)]

    # 시작하는 인덱스와 끝나는 인덱스 저장
    sharp_cnt = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == '#':
                sharp_cnt += 1
                end = [i, j]
            if sharp_cnt == 1:
                start = [i, j]

    isSquare = True
    if start[1] - start[0] != end[1] - end[0]:
        isSquare = False
    for i in range(start[0], end[0] + 1):
        for j in range(start[1], end[1] + 1):
            if graph[i][j] != '#':
                isSquare = False
                break
        if not isSquare:
            break

    if isSquare:
        print(f'#{t} yes')
    else:
        print(f'#{t} no')
