# 완전탐색, DFS

def dfs(idx, string, groups):
    # 전역 변수 생성해서 배열에 단어들을 넣기
    global words
    string += groups[idx]
    words.append(string)

    # 단어의 길이는 5를 넘어갈 수 없음
    if len(string) == 5:
        return
    
    dfs(0, string, groups)
    dfs(1, string, groups)
    dfs(2, string, groups)
    dfs(3, string, groups)
    dfs(4, string, groups)

def solution(to_find):
    alphabets = ['A', 'E', 'I', 'O', 'U']
    global words
    words = []
    
    for i in range(5):
        dfs(i, '', alphabets)
    
    for idx, word in enumerate(words):
        if word == to_find:
            return idx + 1