
#Aleksander Chrismer
#OOP
#Assignment 5-Iterative Process
print("Using the While Loop")
print("")
dblHourlyPay = float(input("Please enter employee hourly pay: "))
dblRaise = float(input("Please enter expected percent raise per year: "))

dblYearlyPay = (dblHourlyPay * 40) * 52
dblRaisePercent = dblRaise / 100

intYear = 1
while intYear <= 10:
  #  dblYearlyPay = dblYearlyPay  
    print ("Year", intYear, "${:,.2f}".format(dblYearlyPay))
    intYear = intYear + 1
    dblYearlyPay = dblYearlyPay + (dblYearlyPay * dblRaisePercent)

print("")
print("Using the For Loop")
print("")

dblHourlyPay = float(input("Please enter employee hourly pay: "))
dblRaise = float(input("Please enter expected percent raise per year: "))
intYear = 1
dblYearlyPay = (dblHourlyPay * 40) * 52
dblRaisePercent = dblRaise / 100
dblTotalYear = 10

for intYear in range (1,11):
    print("Year", intYear, "${:,.2f}".format(dblYearlyPay))
    intYear = intYear + 1
    dblYearlyPay = dblYearlyPay + (dblYearlyPay * dblRaisePercent)



