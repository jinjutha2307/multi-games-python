def start():
    amount = int(input("Enter your amount: "))
    source_currency = input("Enter your currency (USD/EUR/CAD): ").upper()
    target_currency = input("Enter target currency (USD/EUR/CAD): ").upper()

    #  1 USD = 0.86 EUR = 1.36 CAD
    #  1 EUR = 1.16 USD = 1.58 CAD
    #  1 CAD = 0.73 USD = 0.63 EUR
    fixed_rate = {
        "USD": {"USD": 1, "EUR": 0.86, "CAD": 1.36},
        "EUR": {"EUR": 1, "USD": 1.16, "CAD": 1.58},
        "CAD": {"CAD": 1, "USD": 0.73, "EUR": 0.63},
    }

    result = round(amount * fixed_rate[source_currency][target_currency], 2)
    print(f"{amount} {source_currency} is equal to {result} {target_currency}")
