import requests

symbols = {"USD": "$", "CAD": "$", "SGD": "$", "NZD": "$", "AUD": "$", "HKD": "$", "MXN": "$",
           "BRL": "R$",
           "RUB": "₽",
           "GBP": "£",
           "CNY": "¥", "JPY": "¥",
           "EUR": "€",
           "KRW": "₩",
           "INR": "₹",
           "SEK": "kr", "DKK": "kr", "NOK": "kr", "ISK": "kr",
           "ILS": "₪",
           "PLN": "zł",
           "CZK": "Kč",
           "IDR": "Rp",
           "PHP": "₱",
           "HRK": "kn",
           "TRY": "₺",
           "ZAR": "R",
           "CHF": "CHF",
           "BGN": "лв",
           "HUF": "Ft",
           "THB": "฿",
           }


def getRate(fromCurrency, toCurrency):
    # fetch exchange rate from API
    r = requests.get(
        url="https://api.exchangeratesapi.io/latest?base="+fromCurrency)

    # parse data
    data = r.json()

    try:
        data["rates"][toCurrency]
    except:
        return None
    return data["rates"][toCurrency]


def formatMoney(unformatted):
    # make money appear with 2dp
    rounded = round(unformatted, 2)
    # remove excess decimal places and stringify
    money = str(int(rounded * 100))

    # if money < 1, add first character of 0, else we get $.xy
    if money[:-2] == "":
        money = "0" + money

    # return value with decimal point
    return money[:-2] + "." + money[-2:]


def displayMoney(unformatted, currency):
    formattedAmount = formatMoney(unformatted)
    return getSymbol(currency) + formattedAmount


def getSymbol(currency):
    if type(currency) != str or len(currency) != 3:
        raise TypeError("Tried to get symbol for non ISO code")

    currency = currency.upper()

    # If we've found a symbol, return it, else just use the 3 letter currency code
    try:
        return symbols[currency]
    except:
        return currency + " "
