#leap year or not


def isLeapYear(year):
  if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    return True
  else:
    return False


year = int(input("Enter a year : "))

if (isLeapYear):
  print("{} is a leap year.".format(year))
else:
  print("{} is Not a leap year.".format(year) )