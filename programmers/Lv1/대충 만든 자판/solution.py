def solution(keymap, targets):
    hash_map = {}
    for key in keymap:
        for i in range(len(key)):
            if key[i] in hash_map:
                hash_map[key[i]].append(i + 1)
            else:
                hash_map[key[i]] = [i + 1]
    
    result = []
    for target in targets:
        cnt = 0
        for i in range(len(target)):
            if target[i] in hash_map:
                cnt += min(hash_map[target[i]])
            else:
                cnt = -1
                break
        result.append(cnt)
    return result