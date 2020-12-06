
def commaAfter2Digits(money):
    string = "%.2f" % money
    return  string

termYears = 5
interest = 3.5
termMonths = termYears * 12
monthlyRate = 300
accountBalance = 300

for i in range(1, termMonths+1):
    print(str(i)+". month, account balance: "+commaAfter2Digits(accountBalance)+" Euro")
    if i % 12 == 0:
        accountBalance = accountBalance + ((accountBalance/100)*interest)
        print("\n"+str(int(i/12))+". year, account balance: "+commaAfter2Digits(accountBalance)+" Euro\n")
    accountBalance = accountBalance + monthlyRate
