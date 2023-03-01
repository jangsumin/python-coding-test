# 커트라인

n, k = map(int, input().split())
nums = list(map(int, input().split()))

print(sorted(nums, reverse=True)[k - 1])