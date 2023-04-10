# 연월일 달력(D1)

tc = int(input())
for i in range(1, tc + 1):
  date = input()
  year, month, day = date[:4], date[4:6], date[6:]
  
  isMonthCorrect = False
  isDayCorrect = False
  if 1 <= int(month) <= 12:
    isMonthCorrect = True
  if int(month) in [1, 3, 5, 7, 8, 10, 12] and 1 <= int(day) <= 31:
    isDayCorrect = True
  elif int(month) in [4, 6, 9, 11] and 1 <= int(day) <= 30:
    isDayCorrect = True
  elif int(month) == 2 and 1 <= int(day) <= 28:
    isDayCorrect = True

  if isMonthCorrect and isDayCorrect:
    print(f'#{i} {year}/{month}/{day}')
  else:
    print(f'#{i} -1')