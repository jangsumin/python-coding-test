# 진기의 최고급 붕어빵(D3)

possible = 'Possible'
improssible = "Impossible"
 
def solution(n, m, k, peoples):
    peoples.sort()
    for i in range(n):
        total_bread = (peoples[i] // m) * k
        if total_bread < i + 1:
            return improssible
    return possible
 
for t in range(int(input())):
    n, m, k = map(int, input().split())
    peoples = list(map(int, input().split()))
    answer = solution(n, m, k, peoples)
    print('#{} {}'.format(t+1, answer))