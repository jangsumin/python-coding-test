def solution(phone_book):
    # 시간 초과 코드
    # for i in range(0, len(phone_book) - 1):
    #     for j in range(i + 1, len(phone_book)):
    #         min_len = min(len(phone_book[i]), len(phone_book[j]))
    #         if phone_book[i][:min_len] == phone_book[j][:min_len]:
    #             return False
    # return True
    
    # 시간 초과 코드 2
    # phone_book.sort(key=len)
    # for i in range(0, len(phone_book) - 1):
    #     for j in range(i + 1, len(phone_book)):
    #         if phone_book[i] == phone_book[j][:len(phone_book[i])]:
    #             return False
    # return True
    
    # 해쉬를 이용한 풀이
    # hash_map = {}
    # for phone_number in phone_book:
    #     hash_map[phone_number] = 1
    
    # for phone_number in phone_book:
    #     jubdoo = ""
    #     for number in phone_number:
    #         jubdoo += number
    #         if jubdoo in hash_map and jubdoo != phone_number:
    #             return False
    # return True

    phone_book = sorted(phone_book)
    for i in range(len(phone_book) - 1):
        str = phone_book[i]
        if str == phone_book[i+1][:len(str)]:
            return False

    return True