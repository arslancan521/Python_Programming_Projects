
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
letters_2 = letters * 2

def shift(word, shift, action):
    if action == "encryption":
        new_letters = []
        for i in word:
            for ind, char in enumerate(letters):
                if char == i:
                   new_letters.append(letters_2[ind + shift ])
        return "".join(new_letters)
    else:
        new_letters = []
        for i in word:
            for ind, char in enumerate(letters):
                if char == i:
                    new_letters.append(letters[ind - shift])
        return "".join(new_letters)

while True:
    word = str(input("Please enter the word : "))
    amount = int(input("Please enter the amount of shift : "))
    action = str(input("Please enter the action you desire : "))
    result = shift(word,amount,action)
    print(result)