# 시간초과 코드
import math

def solution(answers):
    # 반복되는 패턴 저장
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    # 문제 수만큼 패턴 늘리기
    for i in range(math.ceil(len(answers) / len(pattern1)) - 1):
        pattern1 += pattern1
    for i in range(math.ceil(len(answers) / len(pattern2)) - 1):
        pattern2 += pattern2
    for i in range(math.ceil(len(answers) / len(pattern3)) - 1):
        pattern3 += pattern3
    
    score1, score2, score3 = 0, 0, 0
    for i in range(len(answers)):
        if answers[i] == pattern1[i]: score1 += 1
        if answers[i] == pattern2[i]: score2 += 1
        if answers[i] == pattern3[i]: score3 += 1
    
    res = []
    if score1 == max(score1, score2, score3):
        res.append(1)
    if score2 == max(score1, score2, score3):
        res.append(2)
    if score3 == max(score1, score2, score3):
        res.append(3)
        
    return res