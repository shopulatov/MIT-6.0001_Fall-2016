"""
Created on Thu Feb  3 19:45:53 2022

"""
annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream home:​ '))
semi_annual_raise = float(input('Enter the semi­annual raise, as a decimal:​ '))

portion_down_payment = 0.25
current_savings = 0
r = 0.04
months = 0

while (total_cost * portion_down_payment >= current_savings):
    if months % 6 == 0 and months>1:
        annual_salary *=(1+semi_annual_raise)
        
    current_savings *= (1+r/12)
    current_savings += annual_salary * portion_saved / 12
    months += 1

print(f"Number of months: {months}")
