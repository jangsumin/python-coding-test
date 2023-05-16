def solution(book_time):
    for i in range(len(book_time)):
        sh, sm = book_time[i][0].split(':')
        eh, em = book_time[i][1].split(':')
        book_time[i] = [int(sh) * 60 + int(sm), int(eh) * 60 + int(em) + 10]

    overbooked = 0
    for i in range(24 * 60):
        cnt = 0
        for bt in book_time:
            bs, be = bt
            if bs <= i < be:
                cnt += 1
                if cnt > overbooked:
                    overbooked = cnt

    return overbooked