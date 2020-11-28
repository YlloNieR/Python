today = 23
month = 10
grannysBirthdayDay = 27
grannysBirthdayMonth = 10

# 2.1
daysUntilBirthday = grannysBirthdayDay - today
print(daysUntilBirthday,"days until Grannys Birthday.\n", )

# 2.2
myBirthdayDay = 1
myBirthdayMonth = 12
days = 28
yearMonths = 12

if (myBirthdayMonth <= month):
    if (month == myBirthdayMonth & today == myBirthdayDay):
        print("My birthday is today.")
    else:
        if (myBirthdayDay < today):
            daysUntilBirthday = (
                ((yearMonths - month) + myBirthdayMonth) * days) + myBirthdayDay
            print("My birthday is going to be in",daysUntilBirthday,"days.")
        else:
            daysUntilBirthday = myBirthdayDay - today
            if (daysUntilBirthday == 1):
                print("My birthday is tomorrow.")
            else:
                print("My birthday is going to be in",daysUntilBirthday,"days.")
else:
    daysUntilBirthday = (((myBirthdayMonth - month) *
                          days) - today) + myBirthdayDay
    print("My birthday is going to be in",daysUntilBirthday,"days.")
