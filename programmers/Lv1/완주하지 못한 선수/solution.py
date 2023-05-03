# 해시

def solution(participant, completion):
    marathon_dict = dict()
    for name in participant:
        if name not in marathon_dict:
            marathon_dict[name] = 1
        else:
            marathon_dict[name] += 1
    
    for name in completion:
        marathon_dict[name] -= 1
    
    for name in marathon_dict:
        if marathon_dict[name] == 1:
            return name