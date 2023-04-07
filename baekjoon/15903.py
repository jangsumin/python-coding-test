# 카드 합체 놀이, 그리디

n, m = map(int, input().split())
cards = list(map(int, input().split()))

# for i in range(m):
#   cards.sort()
#   cards[0], cards[1] = cards[0] + cards[1], cards[0] + cards[1]

# print(sum(cards))

import heapq

heap = cards[:]
heapq.heapify(heap)
for _ in range(m):
  x = heapq.heappop(heap)
  y = heapq.heappop(heap)
  temp = x + y
  heapq.heappush(heap, temp)
  heapq.heappush(heap, temp)
print(sum(heap))