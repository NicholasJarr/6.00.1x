def update_balance_each_month(previous_balance, annual_rate, minimum_rate):
    month_interest_rate = annual_rate / 12
    minimum_monthly_payment = minimum_rate * previous_balance
    monthly_unpaid_balance = previous_balance - minimum_monthly_payment

    return monthly_unpaid_balance + (month_interest_rate * monthly_unpaid_balance)

def balance_after_year(balance, annual_rate, minimum_rate):
    current_balance = balance
    for i in range(12):
        current_balance = update_balance_each_month(current_balance, annual_rate, minimum_rate)
    print("Remaining balance:", round(current_balance, 2))
    return round(current_balance, 2)

balance_after_year(balance, annualInterestRate, monthlyPaymentRate)

