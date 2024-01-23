"""
This is a console-based simulator of wordscapes games, where the User
is given some letters and the user has to guess the words from those letters
"""

letters = [
    ['h', 'o', 'l', 'i', 'd', 'a', 'y'],
    ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g'],
    ['b', 'o', 'o', 't', 'c', 'a', 'm', 'p'],
    ['f', 'l', 'o', 'w', 'c', 'h', 'a', 'r', 't'],
    ['w', 'o', 'r', 'd', 's', 'c', 'a', 'p', 'e', 's']
]

words = [
    ["hi", "hay", "day", "had", "lay", "dal", "lad", "lid", "hold", "lady", "hail"],
    ["go", "an", "in", "no", "on", "map", "mom", "gap", "gag", "pig", "man", "ping", "pong", "pram", "prom", "ramp"],
    ["am", "at", "to", "cab", "cap", "cob", "cop", "map", "mop", "act", "bat", "camp", "comb", "boom", "pact", "atom"],
    ["of", "at", "or", "to", "caw", "cow", "how", "who", "calf", "claw", "flaw", "flow", "fowl", "wolf", "crow", "half"],
    ["we", "do", "as", "cap", "caw", "cop", "cow", "paw", "cod", "dew", "pad", "cape", "cope", "crap", "crew", "crop", "pace"]
]


lives = 5
level = 0
score = 0

while level < 5:
    print("level {}".format(level + 1))
    print("Create 3 words using the given letters")

    for i in letters[level]:
        print("{}\t".format(i), end=' ')
    print()

    wordCount = 0
    match = False
    word = ''
    oldWord = ''

    while wordCount == 0 or wordCount < 3:
        match = False
        word = input('word: ')

        if not(word.lower() == oldWord.lower()):
            for w in words[level]:
                if word.lower() == w:
                    wordCount += 1
                    score += 1
                    oldWord = word
                    match = True
                    break

        if not match:
            print('Wrong Guess')
            lives -= 1

        if lives == 0:
            print("Game over!! Better luck next time!!")
            print("Your score is {}".format(score))

    wordCount = 0
    match = False
    word = ''

    if lives == 0:
        break

    if level == 4:
        print("Thanks for playing th game !!!")
        print("Your score is {}".format(score))
        level += 1
    else:
        choice = input("Do you want to continue to next level? (y/n)")
        if choice.lower()[0] == 'y':
            level += 1

        else:
            print('Thanks for playing the game!!!')
            print("Your score is {}".format(score))
            break