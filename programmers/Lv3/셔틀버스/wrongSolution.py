# 정확성 75%의 코드

def solution(n, t, m, timetable):
    tt = []
    # timetable 정렬, 분으로 환산
    for time in timetable:
        hour, minute = map(int, time.split(":"))
        tt.append(hour * 60 + minute)
    tt.sort()

    already_go = [False] * len(tt)
    ans = 0
    # 분으로 환산
    bus_start = 9 * 60
    for i in range(bus_start, bus_start + n * t, t):
        cnt = 0
        for j in range(len(tt)):
            if tt[j] <= i and already_go[j] == False:
                cnt += 1
                already_go[j] = True 
            if cnt == m:
                break

        if i == bus_start + (n - 1) * t:
            if cnt == m:
                idx = 0
                for j in range(len(already_go)):
                    if already_go[j] == True:
                        idx = j
                ans = tt[j] - 1
            else:
                ans = i

    str_hour = str(ans // 60)
    str_minute = str(ans % 60)
    if len(str_hour) == 1:
        str_hour = '0' + str_hour
    if len(str_minute) == 1:
        str_minute = '0' + str_minute

    return str_hour + ":" + str_minute