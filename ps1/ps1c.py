"""
Created on Thu Feb  3 19:55:55 2022

"""
annual_salary = float(input('Enter your starting salary: '))

epsilon = 100
total_cost = 1_000_000
semi_annual_raise = 0.07
portion_down_payment = 0.25
current_savings = 0
r = 0.04
months = 36
new_current_savings = 1
steps = 0

down_payment = total_cost * portion_down_payment

for n in range(1,months+1):
    current_savings *= (1+r/12)
    current_savings += annual_salary / (12*10000)
    
    if n % 6 == 0 and n>=1:
        annual_salary *= (1+semi_annual_raise)

low = 0
high = 10000
mid = (low+high)//2

while abs(down_payment - new_current_savings) >= epsilon:
    steps +=1
    new_current_savings = current_savings * mid
    
    prev_portion_saved = mid
    if new_current_savings < down_payment:
        low = mid
    else:
        high= mid
    
    mid = int(round((low+high)/2))
    
    if prev_portion_saved == mid:
        break

if mid == 10000:
    print("Not possible to acquire the house within 36 months.")
else:
    print(f"Best savings rate: {round(mid / 10000, 4)}")
    print(f"Steps in Bisection search: {steps}")
