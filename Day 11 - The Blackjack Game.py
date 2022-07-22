import random


def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10]
    card = random.choice(cards)
    return card

def score(cards):
    score = 0
    for i in cards:
        score += i
    return score

def check_score(user_score, comp_score):

    if user_score == 21 or comp_score == 21:
        return "Blackjack"
    elif user_score > 21 or comp_score > 21:
        return "Boom"
    else:
        return True

def compare(user_score, comp_score, user_cards, comp_cards):

    if user_score < comp_score:
        return f"Computer has won with {comp_cards} : {comp_score} against {user_cards} : {user_score}"
    elif user_score > comp_score:
        return f"Computer has lost with {comp_cards} : {comp_score} against {user_cards} : {user_score}"
    else:
        return f"No one has won"


while True:
    user_cards = []
    comp_cards = []
    game = str(input("Would you like to play ? "))
    if game == "no":
        break
    else:

        for i in range(2):
            user_cards.append(deal_card())
            comp_cards.append(deal_card())

    print(f"User's cards : {user_cards} with total : {score(user_cards)}")
    print(f"Computer's first card is : {comp_cards[0]}")
    while True:
        new_card = str(input("Would you like to take another card ? "))
        if new_card == "no":
            user_score = score(user_cards)
            comp_score = score(comp_cards)

            result = compare(user_score, comp_score, user_cards, comp_cards)

            print(result)
            break
        else:
            user_cards.append(deal_card())
            print(f"User's cards : {user_cards} with total : {score(user_cards)}")
            print(f"Computer's first card is : {comp_cards}")

    user_score = score(user_cards)
    comp_score = score(comp_cards)

    while comp_score > 17:
        comp_cards.append(deal_card())

    user_score = score(user_cards)
    comp_score = score(comp_cards)

    result = compare(user_score,comp_score,user_cards,comp_cards)

    print(result)


