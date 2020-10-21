#program that reads two integers representing a month and day and prints the season for that month and day

month = input("Input the month (e.g. 1, 2 etc.): ")
day = int(input("Input the day: "))

if month in ('1', '2', '3'):
	season = 'winter'
elif month in ('4', '5', '6'):
	season = 'spring'
elif month in ('7', '8', '9'):
	season = 'summer'
else:
	season = 'autumn'

if (month == '3') and (day > 19):
	season = 'spring'
elif (month == '6') and (day > 20):
	season = 'summer'
elif (month == '9') and (day > 21):
	season = 'autumn'
elif (month == '12') and (day > 20):
	season = 'winter'

print("Season is",season)
