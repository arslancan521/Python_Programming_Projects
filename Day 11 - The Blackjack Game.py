<<<<<<< HEAD
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


=======

import random


def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card


def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""

  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  #Bug fix. If you and the computer are both over, you lose.
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"


  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def play_game():



  user_cards = []
  computer_cards = []
  is_game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())


  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  play_game()
>>>>>>> origin/master
