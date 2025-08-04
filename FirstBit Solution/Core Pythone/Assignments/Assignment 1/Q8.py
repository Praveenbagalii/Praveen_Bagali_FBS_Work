#Convert days into Years, Weeks, and Days
days = int(input("Enter number of days: "))

years = days // 365
weeks = (days % 365) // 7
days = (days % 365) % 7

print(f'{years} Years, {weeks} Weeks and {days} Days')