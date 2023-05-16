def solution(s, skip, index):
    alphabet_group = []
    
    for i in range(97, 123):
        if chr(i) not in skip:
            alphabet_group.append(chr(i))
            
    answer = ''
    for i in range(len(s)):
        to_find = alphabet_group.index(s[i]) + index
        if to_find >= 26 - len(skip):
            to_find %= 26 - len(skip)
        answer += alphabet_group[to_find]
    return answer