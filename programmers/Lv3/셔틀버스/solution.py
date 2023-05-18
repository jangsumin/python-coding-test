# 충분히 더 간단한 분기 처리로 풀 수 있음.

def solution(n, t, m, timetable):
    ans = 0
    tt = [int(time[:2]) * 60 + int(time[3:]) for time in timetable]
    tt.sort()
    busTime = [9 * 60 + t * i for i in range(n)]

    i = 0
    for tm in busTime:
      cnt = 0
      while cnt < m and i < len(tt) and tt[i] <= tm:
        i += 1
        cnt += 1
      if cnt < m: ans = tm
      else: ans = tt[i - 1] - 1

    return str(ans // 60).zfill(2) + ":" + str(ans % 60).zfill(2)