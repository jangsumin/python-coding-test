# 최대 성적표 만들기(D3)

tc = int(input())
for t in range(1, tc + 1):
  n, k = map(int, input().split())
  score_list = list(map(int, input().split()))

  score_list.sort(reverse=True)
  sum = 0
  for i in range(k):
    sum += score_list[i]
  
  print(f'#{t} {sum}')