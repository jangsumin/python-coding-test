# 두 개 뽑아서 더하기, 정렬

def solution(numbers):
    res = []
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] not in res:
                res.append(numbers[i] + numbers[j])
    return sorted(res)