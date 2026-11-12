total = 0
days = 0

while True:
    savings = float(input("Savings today (0 to stop): "))

    if savings == 0:
        break

    total += savings
    days += 1

print(f"Total saved in {days} days: PHP {total:,.2f}")