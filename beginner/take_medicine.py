# Problem: https://www.codechef.com/problems/MEDIC

def isLeapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def count_pills(date):
    strArr = date.split(':')
    year, mon, day = map(int, date.split(':'))
    if mon in [1, 3, 5, 7, 8, 10, 12]:
        pills = 32 - day
    elif mon in [4, 6, 9, 11]:
        pills = 62 - day
    elif mon == 2:
        if isLeapYear(year):
            pills = 30 - day
        else:
            pills = 60 - day
    return pills//2 + pills % 2


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        date = input()
        print(count_pills(date))
