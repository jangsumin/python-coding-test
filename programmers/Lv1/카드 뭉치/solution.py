def solution(cards1, cards2, goal):
    i, j, isPossible = 0, 0, True
    for word in goal:
        if i < len(cards1) and cards1[i] == word:
            i += 1
        elif j < len(cards2) and cards2[j] == word:
            j += 1
        else:
            isPossible = False
    if isPossible:
        return 'Yes'
    else:
        return 'No'