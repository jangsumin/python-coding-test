def dfs(v, computers, visited):
    visited[v] = True
    for i in range(len(computers[v])):
        if v == i:
            continue
        if visited[i] == False and computers[v][i] == 1:
            dfs(i, computers, visited)

def solution(n, computers):
    answer = 0
    
    visited = [False] * n
    for i in range(n):
        if visited[i] == False:
            dfs(i, computers, visited)
            answer += 1
    
    return answer