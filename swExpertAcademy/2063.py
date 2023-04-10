# 중간값 찾기(D1)

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
length = len(arr)
print(arr[length // 2])