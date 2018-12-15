interestRate = float(input("Enter the annual interest rate(%) : "))
bankBalance = float(input("Enter the amount of deposit : "))
taxRate = float(input("Enter the tax percentage(%) : "))
durationMonths = int(input("After how many months you are going to withdraw money back? : "))
renewalMonths = int(input("Enter the renewal period in months : "))

addedValue = 0.0
years = 0
months = 0
totalAdditionalValue = 0.0
remainingMonthProfit = 0.0
totalRenewals = durationMonths // renewalMonths
remainingMonthes = durationMonths % renewalMonths

print("")

for x in range(totalRenewals):
    addedValue = (((bankBalance * (interestRate / 100.0)) / (12 / renewalMonths)) * ((100.0 - taxRate) / 100.0))
    bankBalance += addedValue
    totalAdditionalValue += addedValue
    print("Amount after renewal : ", 'Rs.{:,.2f}'.format(bankBalance), " [Added value : ", 'Rs.{:,.2f}'.format(addedValue), "]")

    if ((x + 1) % (12 / renewalMonths)) == 0:
        print("(year)")

if remainingMonthes == 1:
    remainingMonthProfit = (bankBalance * (interestRate / 100.0)) / 12
    print("Remaining month profit : ", 'Rs.{:,.2f}'.format(remainingMonthProfit))
    bankBalance += remainingMonthProfit
elif remainingMonthes == 2:
    remainingMonthProfit = (bankBalance * (interestRate / 100.0)) / 6
    print("Remaining month profit added : ", 'Rs.{:,.2f}'.format(remainingMonthProfit))
    bankBalance += remainingMonthProfit


totalAdditionalValue += remainingMonthProfit
years = durationMonths // 12

print("")

if years > 0:
    months = durationMonths - (12 * years)

    if months > 0:
        print("After", years, "years and", months, "months:-")
    else:
        print("After", years, "years:-")

else:
    print("After", months, "months:-")

print("Total profit you have gained : ", 'Rs.{:,.2f}'.format(totalAdditionalValue))
print("Monthly average profit : ", 'Rs.{:,.2f}'.format(totalAdditionalValue / durationMonths))
print("Total balance : ", 'Rs.{:,.2f}'.format(bankBalance))

