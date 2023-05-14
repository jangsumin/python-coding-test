# 상호의 배틀필드(D3)

tc = int(input())
for t in range(1, tc + 1):
    h, w = map(int, input().split())
    game_map = [list(input()) for _ in range(h)]
    n = int(input())
    command = input()

    # 전차 위치 찾기
    car = [0, 0]
    for i in range(h):
        for j in range(w):
            if game_map[i][j] in ('<', '>', 'v', '^'):
                car[0] = i
                car[1] = j

    for i in range(len(command)):
        if command[i] == 'S':
            if game_map[car[0]][car[1]] == '^':
                for j in range(car[0] - 1, -1, -1):
                    if game_map[j][car[1]] == '#':
                        break
                    if game_map[j][car[1]] == '*':
                        game_map[j][car[1]] = '.'
                        break
            if game_map[car[0]][car[1]] == 'v':
                for j in range(car[0] + 1, h):
                    if game_map[j][car[1]] == '#':
                        break
                    if game_map[j][car[1]] == '*':
                        game_map[j][car[1]] = '.'
                        break
            if game_map[car[0]][car[1]] == '<':
                for j in range(car[1] - 1, -1, -1):
                    if game_map[car[0]][j] == '#':
                        break
                    if game_map[car[0]][j] == '*':
                        game_map[car[0]][j] = '.'
                        break
            if game_map[car[0]][car[1]] == '>':
                for j in range(car[1] + 1, w):
                    if game_map[car[0]][j] == '#':
                        break
                    if game_map[car[0]][j] == '*':
                        game_map[car[0]][j] = '.'
                        break

        if command[i] == 'U':
            game_map[car[0]][car[1]] = '^'
            if car[0] - 1 >= 0 and game_map[car[0] - 1][car[1]] == '.':
                game_map[car[0]][car[1]] = '.'
                car = [car[0] - 1, car[1]]
                game_map[car[0]][car[1]] = '^'
        if command[i] == 'D':
            game_map[car[0]][car[1]] = 'v'
            if car[0] + 1 <= h - 1 and game_map[car[0] + 1][car[1]] == '.':
                game_map[car[0]][car[1]] = '.'
                car = [car[0] + 1, car[1]]
                game_map[car[0]][car[1]] = 'v'
        if command[i] == 'L':
            game_map[car[0]][car[1]] = '<'
            if car[1] - 1 >= 0 and game_map[car[0]][car[1] - 1] == '.':
                game_map[car[0]][car[1]] = '.'
                car = [car[0], car[1] - 1]
                game_map[car[0]][car[1]] = '<'
        if command[i] == 'R':
            game_map[car[0]][car[1]] = '>'
            if car[1] + 1 <= w - 1 and game_map[car[0]][car[1] + 1] == '.':
                game_map[car[0]][car[1]] = '.'
                car = [car[0], car[1] + 1]
                game_map[car[0]][car[1]] = '>'

    print(f'#{t}', end=' ')
    for i in range(h):
        print(''.join(game_map[i]))
