# GNS

dic = {
    "ZRO": 0,
    "ONE": 1,
    "TWO": 2,
    "THR": 3,
    "FOR": 4,
    "FIV": 5,
    "SIX": 6,
    "SVN": 7,
    "EGT": 8,
    "NIN": 9
}

tc = int(input())
for _ in range(1, tc + 1):
    t, length = input().split()
    length = int(length)

    str_list = list(input().split())
    str_list.sort(key = lambda x: dic[x])

    print(t)
    print(*str_list)