import calendar

date = list(map(int, input().split()))

number_day = calendar.weekday(date[2], date[0], date[1])

print(calendar.day_name[number_day].upper())
