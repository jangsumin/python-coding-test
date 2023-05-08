def solution(name, yearning, photo):
    res = []
    for group in photo:
        score = 0
        for missing in group:
            if missing in name:
                score += yearning[name.index(missing)]
        res.append(score)
    return res