# 조교의 성적 매기기(D2)

tc = int(input())
grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for t in range(1, tc + 1):
    n, k = map(int, input().split())
    total_list = []
    for _ in range(n):
        mid, final, hws = map(int, input().split())
        total = (mid * 0.35) + (final * 0.45) + (hws * 0.2)
        total_list.append(total)

    k_score = total_list[k - 1]
 
    total_list.sort(reverse=True)
    div = n // 10
    final_k_score = total_list.index(k_score) // div

    print('#{} {}'.format(t, grades[final_k_score]))