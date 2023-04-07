# 카드 합체 놀이, 그리디

n, m = map(int, input().split())
cards = list(map(int, input().split()))

for i in range(m):
  cards.sort()
  cards[0], cards[1] = cards[0] + cards[1], cards[0] + cards[1]

print(sum(cards))