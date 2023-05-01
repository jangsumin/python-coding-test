def solution(s, n):
    s_list = list(s)
    res = ''
    for el in s_list:
        if el == ' ':
            res += el
            continue
            
        before_pswd = ord(el)
        after_pswd = ord(el) + n
        if 97 <= before_pswd <= 122 and after_pswd > 122:
            after_pswd -= 26
        elif 65 <= before_pswd <= 90 and after_pswd > 90:
            after_pswd -= 26
        res += chr(after_pswd)
    return res