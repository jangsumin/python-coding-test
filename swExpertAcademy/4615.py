# 재미있는 오셀로 게임(D3)

tc = int(input())
for t in range(1, tc + 1):
    n, m = map(int, input().split())
    graph = [[0] * (n + 2) for _ in range(n + 2)]
    graph[n // 2][n // 2] = 2
    graph[n // 2 + 1][n // 2] = 1
    graph[n // 2][n // 2 + 1] = 1
    graph[n // 2 + 1][n // 2 + 1] = 2
    for _ in range(m):
        x, y, color = map(int, input().split())
        graph[y][x] = color

        # 오른쪽, 왼쪽, 위, 아래, 대각선 왼쪽 아래, 대각선 왼쪽 위, 대각선 오른쪽 아래, 대각선 오른쪽 위
        dx = [1, -1, 0, 0, -1, -1, 1, 1]
        dy = [0, 0, 1, -1, -1, 1, -1, 1]
        for i in range(8):
            changes = []
            k = 1
            while graph[y + k * dy[i]][x + k * dx[i]] != 0 and graph[y + k * dy[i]][x + k * dx[i]] != color and \
              1 <= y + k * dy[i] <= n and 1 <= x + k * dx[i] <= n:
                changes.append([y + k * dy[i], x + k * dx[i]])
                k += 1

            if graph[y + k * dy[i]][x + k * dx[i]] == color:
                for nx, ny in changes:
                    graph[nx][ny] = color
                    
        # print(graph)
        
    white_cnt, black_cnt = 0, 0
    for i in range(n + 2):
        for j in range(n + 2):
            if graph[j][i] == 2:
                white_cnt += 1
            if graph[j][i] == 1:
                black_cnt += 1
    print(f'#{t} {black_cnt} {white_cnt}')