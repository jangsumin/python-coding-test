def solution(rows, columns, queries):
    answer = []
    
    graph = []
    for i in range(0, rows):
        row = []
        for j in range(1, columns + 1):
            row.append(i * columns + j)
        graph.append(row)
    
    for query in queries:
        num_list = []
        x1, y1, x2, y2 = query
        
        first = graph[x1 - 1][y1 - 1]
        min_value = first
        
        for k in range(x1, x2):
            graph[k - 1][y1 - 1] = graph[k][y1 - 1]
            min_value = min(min_value, graph[k][y1 - 1])
        for k in range(y1, y2):
            graph[x2 - 1][k - 1] = graph[x2 - 1][k]
            min_value = min(min_value, graph[x2 - 1][k])
        for k in range(x2, x1, -1):
            graph[k - 1][y2 - 1] = graph[k - 2][y2 - 1]
            min_value = min(min_value, graph[k - 2][y2 - 1])
        for k in range(y2, y1 + 1, -1):
            graph[x1 - 1][k - 1] = graph[x1 - 1][k - 2]
            min_value = min(min_value, graph[x1 - 1][k - 2])
    
        graph[x1 - 1][y1] = first
        answer.append(min_value)
        
    return answer