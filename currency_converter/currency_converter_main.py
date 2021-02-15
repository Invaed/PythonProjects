from forex_python.converter import CurrencyRates
c = CurrencyRates()
try:
    amount = int(input("Please enter amount: "))
    from_currency = input("Please enter From currency: ").upper()
    to_currency = input("Please enter To currency: ").upper()
    result = c.convert(base_cur=from_currency, dest_cur=to_currency, amount=amount)
    print(f"{from_currency} {amount} = {to_currency} {result}")
except:
    print("Invalid input provided")