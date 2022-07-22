
auctions = {}

def add_auction(name, amount):
    if name not in auctions.keys():
        auctions[name] = amount
    else:
        auctions.update({name : amount})

def get_winner():
    max_offer = max(list(auctions.values()))
    for i,j in auctions.items():
        if j == max_offer:
            return f"{i} has won the auction with {j} $ offer."



while True:

    name = str(input("Please enter your name : "))
    amount = int(input("Please enter your offer : "))
    add_auction(name, amount)
    print(f"Last offer is {amount}")
    gameplay = str(input("Do you have any other offer :"))

    if gameplay == "yes":
        continue

    else:
        print(auctions)
        print(get_winner())
        break