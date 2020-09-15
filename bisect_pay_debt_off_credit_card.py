def minimum_month_payment(balance, annual_rate):
    monthly_rate = annual_rate / 12
    lower_bound = balance / 12
    upper_bound = (balance * (1 + monthly_rate)**12) / 12

    while True:
        fixed_payment = (upper_bound + lower_bound) / 2
        unpaid_balance = balance
        for i in range(12):
            unpaid_balance -= fixed_payment
            unpaid_balance = unpaid_balance + monthly_rate * unpaid_balance

        if round(unpaid_balance, 2) == 0:
            break
        if unpaid_balance < 0:
            upper_bound = fixed_payment
        else:
            lower_bound = fixed_payment
    return round(fixed_payment, 2)

print("Lowest payment:", minimum_month_payment(balance, annualInterestRate))
