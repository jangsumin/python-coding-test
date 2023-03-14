# 단어 나누기

# psudo code
# 가장 작은 알파벳 찾고 거기서 끊기
# 위 과정 반복

s = input()
arr = list(s)
save = list()

for i in range(1, len(arr) - 1):
  for j in range(i + 1, len(arr)):
    s1 = arr[: i]
    s2 = arr[i : j]
    s3 = arr[j :]
    s1.reverse()
    s2.reverse()
    s3.reverse()
    save.append(''.join(s1 + s2 + s3))

print(sorted(save)[0])