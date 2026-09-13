seasons = ["Winter", "Spring",
           "Summer", "Autumn"]
print("What month is it? (1-12)")
month = int(input())
if month == 12 or month == 1 or month == 2:
  season = 0
elif month == 3 or month == 4 or month == 5:
  season = 1
elif month == 6 or month == 7 or month == 8:
  season = 2
elif month == 9 or month == 10 or month == 11:
  season = 3
else:
    season = "You are an idiot. Ha, ha ha, ha, ha ha ha!"
print("It is", seasons[season])
