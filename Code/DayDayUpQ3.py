#DayDayUpQ3.py
dayup =1.0
dayfacter = 0.01
for i in range(365):
    if i % 7 in [6, 0]:
        dayup *= 1-dayfacter
    else:
        dayup *= 1+dayfacter
print("工作日的力量：{:.2f}".format(dayup))