monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
print("Your monthly savings are","$",monthly_savings) 
Projected_Savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print("Projected_Savings after one year, with interest, is: ","$",Projected_Savings)