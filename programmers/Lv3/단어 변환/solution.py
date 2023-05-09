# bfs로 접근

from collections import deque
def solution(begin, target, words):
    # target이 words에 없으면 0 반환
    if target not in words:
        return 0
    
    queue = deque()
    queue.append(begin)
    visited = []
    cnt = 0
    while True:
        if target in queue:
            break
        for _ in range(len(queue)):
            chg_word = queue.popleft()
            visited.append(chg_word)
            for word in words:
                diff_cnt = 0
                for i in range(len(word)):
                    if chg_word[i] != word[i]:
                        diff_cnt += 1
                if diff_cnt == 1 and word not in visited:
                    queue.append(word)
        cnt += 1
    return cnt