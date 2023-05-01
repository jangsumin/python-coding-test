def solution(s):
    # 하나 이상의 공백문자로 구분되어 있다는 점을 유의
    s_list = list(s)
    i, j = 0, 0
    while i < len(s_list):
        if s_list[i] == ' ':
            j = 0
        else:
            if j % 2 == 0:
                s_list[i] = s_list[i].upper()
            if j % 2 == 1:
                s_list[i] = s_list[i].lower()
            j += 1
        # i는 계속 증가
        i += 1
    return ''.join(s_list)