income = int(input('enter your income : '))

if income < 67000:
    tax = income * (1-0.24)
elif income < 97000:
    taxe = income * (1-0.31)
elif income > 97000:
    tax = income * (1-0.34)
print(f'Your income after taxes is {tax} euros')    
