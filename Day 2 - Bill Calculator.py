def calculator(bill, amount, tip):
    return (bill * tip / 100 ) / amount

bill = int(input("Please enter the bill :"))
amount = int(input("How many people exist : "))
tip = int(input("What percent is the tip : "))
print(calculator)