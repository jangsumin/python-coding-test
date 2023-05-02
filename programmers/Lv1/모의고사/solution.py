# 포인터 사용해서 풀었음

def solution(answers):
    # 반복되는 패턴 저장
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    i, j, k = 0, 0, 0
    score1, score2, score3 = 0, 0, 0
    for idx in range(len(answers)):
        if i == len(pattern1):
            i = 0
        if j == len(pattern2):
            j = 0
        if k == len(pattern3):
            k = 0
        
        if answers[idx] == pattern1[i]:
            score1 += 1
        if answers[idx] == pattern2[j]:
            score2 += 1
        if answers[idx] == pattern3[k]:
            score3 += 1
        i += 1
        j += 1
        k += 1
    
    score = [score1, score2, score3]
    res = []
    for i in range(3):
        if score[i] == max(score):
            res.append(i + 1)
    return res