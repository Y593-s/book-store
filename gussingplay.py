import random

name = input("what is your name? ")
print("good luck!" + name)

names = ['hadi', 'yara', 'hassan', 'sara', 'osama']

word = random.choice(names)

print("the name is")

guesses = ''

turns = 12

while turns > 0:

    failed = 0

    for char in word:

        if char in guesses:
            print(char)

        else:
            print("-")
            failed +=1

    if failed == 0:
        print("you win")
        print("the name is: ", word)
        break

    guess = input("guess a character: ")

    guesses += guess

    if guess not in word:
        turns -=1
        print("wrong guess")
        print("you have", + turns, 'more guesses')

        if turns == 0:
            print("you looses")