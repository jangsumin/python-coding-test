# 대소문자 바꾸기

arr = list(input())

for i in range(len(arr)):
  if arr[i] >= 'A' and arr[i] <= 'Z':
    arr[i] = chr(ord(arr[i]) + 32)
  else:
    arr[i] = chr(ord(arr[i]) - 32)

print(''.join(arr))