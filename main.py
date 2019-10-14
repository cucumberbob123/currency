from conversion import formatMoney, getRate, displayMoney

originalMoney = float(input("How much money would you like to convert? "))
fromCurrency = input("\nWhat currency is that?").upper()
toCurrency = input(
    "\nWhat currency would you like to convert to?").upper()

rate = getRate(fromCurrency, toCurrency)

if rate:
    converted = originalMoney * rate
    print(displayMoney(converted, toCurrency))
else:
    print("We can't convert between those currencies at the moment, sorry.")
