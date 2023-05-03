# 카펫, 완전탐색

def solution(brown, yellow):
    total_size = brown + yellow
    
    res = []
    for i in range(1, total_size + 1):
        if total_size % i == 0:
            if (i - 2) * (total_size // i - 2) == yellow:
                if i >= total_size:
                    res.append(i)
                    res.append(total_size // i)
                else:
                    res.append(total_size // i)
                    res.append(i)
                break
    
    return res