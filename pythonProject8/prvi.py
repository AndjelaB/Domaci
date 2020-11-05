month = input("months: ")
month = int(month)
if month <= 0 or month >= 13:
    print("wrong")
elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("31 days")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("31 days")
else:
    print("28 or 29 days")
