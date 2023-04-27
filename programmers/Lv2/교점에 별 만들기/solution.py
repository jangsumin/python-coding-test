def solution(line):
    
    # 교점 저장 리스트
    points = []
    for i in range(0, len(line) - 1):
        for j in range(i + 1, len(line)):
            # 평행일 경우 제외
            if line[i][0] * line[j][1] - line[i][1] * line[j][0] == 0:
                continue
            
            x_up = line[i][1] * line[j][2] - line[i][2] * line[j][1]
            x_down = line[i][0] * line[j][1] - line[i][1] * line[j][0]
            
            y_up = line[i][2] * line[j][0] - line[i][0] * line[j][2]
            y_down = line[i][0] * line[j][1] - line[i][1] * line[j][0]
            
            # 정수인지 확인하기
            if x_up / x_down == int(x_up / x_down) and y_up / y_down == int(y_up / y_down):
                points.append([int(x_up / x_down), int(y_up / y_down)])
    
    min_x = min([point[0] for point in points])
    min_y = min([point[1] for point in points])
    max_x = max([point[0] for point in points])
    max_y = max([point[1] for point in points])
    
    graph = [[] for _ in range(max_y - min_y + 1)]
    for i in range(0, max_y - min_y + 1):
        for j in range(0, max_x - min_x + 1):
            if [j + min_x, i + min_y] in points:
                graph[i].append('*')
            else:
                graph[i].append('.')
    
    for i in range(0, max_y - min_y + 1):
        graph[i] = ''.join(graph[i])
        
    return list(reversed(graph))