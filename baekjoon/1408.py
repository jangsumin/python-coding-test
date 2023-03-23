# 24

current_h, current_m, current_s = map(int, input().split(':'))
aim_h, aim_m, aim_s = map(int, input().split(':'))

res_h, res_m, res_s = aim_h - current_h, aim_m - current_m, aim_s - current_s

if res_s < 0:
  res_s = 60 + res_s
  res_m -= 1
if res_m < 0:
  res_m = 60 + res_m
  res_h -= 1
if res_h < 0:
  res_h = 24 + res_h

print(':'.join([str(res_h).zfill(2), str(res_m).zfill(2), str(res_s).zfill(2)]))