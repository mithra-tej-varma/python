def leap_year(year):
    if year%400==0:
        return True
    elif year%100==0:
        return False
    elif year%4==0:
        return True
    else:
        return False

def days(year,month):
    days=[31,28,31,30,31,30,31,31,30,31,30,31]
    if leap_year(year) and month==2:
        return 29
    else :
        return days[month-1]
year = int(input("Enter year: "))
month = int(input("Enter month: "))
print(days(year,month))