
def commaAfter2Digits(money):
    string = "%.2f" % money
    return  string

termYears = 5
interest = 3.5
termMonths = termYears * 12
monthlyRate = 300
accountBalance = 300
counter = 1;

while counter != termMonths+1:
    print(str(counter)+". month, account balance: "+commaAfter2Digits(accountBalance)+" Euro")
    if counter % 12 == 0:
        accountBalance = accountBalance + ((accountBalance/100)*interest)
        print("\n"+str(int(counter/12))+". year, account balance: "+commaAfter2Digits(accountBalance)+" Euro\n")
    accountBalance = accountBalance + monthlyRate
    counter += 1
