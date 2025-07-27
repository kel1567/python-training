name = input("Write your name: ").title()
hourly_wage = float(input("Your hourly wage? "))
hours_worked = int(input("How many hours you have worked this week? "))
total_earn = hourly_wage * hours_worked # 2 2.0 # 2.00
print(f"{name.title()} earned ${total_earn:.2f} this week.")
