# 테스트 케이스 하나가 시간 초과가 남.
# 일단 형변환이 너무 많은 데다가, 문자열을 + 연산으로 이어 붙이는 것은 매우 좋지 않은 습관
def solution(number, k):
    number_list = list(map(int, list(number)))
    
    res_len = len(number_list) - k
    res = ''
    
    cnt = 0
    i = 0
    remain = res_len - cnt - 1
    while True:
        if cnt == res_len:
            break
        to_find = max(number_list[i : len(number_list) - remain])
        res += str(to_find)
        for j in range(i, len(number_list) - remain):
            if number_list[j] == to_find:
                i = j + 1
                break
        cnt += 1
        remain = res_len - cnt - 1
    
    return res