# 줄 세우기(위상 정렬 문제)

# 위상 정렬 문제 풀이 방법 중 BFS로 해결
n, m = map(int, input().split())

# 서로의 선후배 관계를 저장
graph = [[] for _ in range(n + 1)]
# 자신보다 앞선 정점이 몇 개 있는지 확인하는 배열 저장
in_degree = [0] * (n + 1)
# 결과 저장
ans = []

for _ in range(m):
  front, back = map(int, input().split())
  graph[front].append(back)
  in_degree[back] += 1

# 큐
from collections import deque
queue = deque()

# 일단 자신보다 앞선 정점이 없는 경우 먼저 정답에 추가 할 수 있음
for i in range(1, n + 1):
  if in_degree[i] == 0:
    queue.append(i)

# 큐에 값이 있는 동안 계속 진행
while queue:
  # 큐의 가장 앞에 있는 값을 꺼내서 그 값과 연결된 정점들을 가져오는데
  # 그 정점들의 앞선 정점 하나가 사라진 것과 마찬가지이므로 -1씩 함
  # 그러다가 0이 되면 정답에 추가할 수 있음
  x = queue.popleft()
  ans.append(x)
  for v in graph[x]:
    in_degree[v] -= 1
    if in_degree[v] == 0:
      queue.append(v)

print(*ans)