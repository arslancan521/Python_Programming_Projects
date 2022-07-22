
#TODO
# CHOOSE WORD
# CREATE TEMPLATE
# DETERMINE CHANCES
# CONTROL CHANCES
# CONTROL GAMEPLAY
# CHECK LETTER
# UPDATE TEMPLATE

import random

word_list = ["crocodile", "computer", "police", "handbook", "python", "java"]

# CHOOSE WORD

def random_word():
    return random.choice(word_list)

# CREATE TEMPLATE

def create_template(len):
    return "_" * len

# CHANCES

chances = 10

# UPDATE CHANCES

def update_chances(letter, word):
    global chances
    if letter in word:
        pass
    else:
        chances -= 1

# CONTROL GAMEPLAY



def update_gameplay(chances,template):

    if chances == 0:
        return False
    elif "_" not in template:
        return False
    else:
        return True

# CHECK LETTER

def check_letter(letter, word):
    positions = []
    if letter in word:
        for i,j in enumerate(word):
            if j == letter:
                positions.append(i)
            else:
                pass
        return positions
    else:
        return False

# UPDATE TEMPLATE

def update_template(template, position, letter):
    template_list = []
    for i in template:
        template_list.append(i)

    for i in position:
        template_list[i] = letter
    return "".join(template_list)

word = random_word()
template = create_template(len(word))



while True:
    gameplay = update_gameplay(chances,template)
    if gameplay == True:
        print(f"You have {chances} left")
        print(template)
        letter = str(input("Please enter a letter :"))
        update_chances(letter,word)
        positions = check_letter(letter,word)
        if positions != False:
            template = update_template(template,positions,letter)
        else:
            print(f"The {letter} doesn't exist, sorry.")
            continue
    else:
        print(f"You have {chances} left")
        print(f"The word is {word}")
        print(f"Current Template is {template}")
        if word == template:
            print("Congrats, you have found the word")
        else:
            print("Unfortunately you could not find the word, try again.")
        break
