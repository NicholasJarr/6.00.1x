def minimum_month_payment(balance, monthly_rate, fixed_payment = 0):
    unpaid_balance = balance
    for i in range(12):
        unpaid_balance -= fixed_payment
        unpaid_balance = unpaid_balance + monthly_rate * unpaid_balance

    if unpaid_balance <= 0:
        return fixed_payment
    else:
        return minimum_month_payment(balance, monthly_rate, fixed_payment + 10)
