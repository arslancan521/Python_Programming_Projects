

def calculate_bill(total, tip, people):
    return round((total * (1 + tip / 100)) / people, 2)


total = float(input("Please enter the total bill : "))
tip = int(input("Please enter the percentage of the tip : "))
people = int(input("Please enter the amount of people pay for the bill : "))

print(calculate_bill(total, tip, people))


