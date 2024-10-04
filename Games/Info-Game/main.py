import random

from game_data import data

from art import Logo, vs

print(Logo)

name = ""
description = ""
country = ""
follower_count = 0
score = 0


def random_dica():
    global name, description, country, follower_count
    random_dica = random.choice(data)
    name = random_dica["name"]
    description = random_dica["description"]
    country = random_dica["country"]
    follower_count = random_dica["follower_count"]


random_dica()
A = name
c = follower_count
print(f"Compare 'A': {name} , a {description} , from {country}.")

print(vs)

random_dica()
B = name

if A == B:
    random_dica()
else:
    print(f"Aginst 'B': {name} , a {description} , from {country}.")
    d = follower_count

winner = input("Who has more followers ? 'A' or 'B' :")


def check_followers():
    global score, winner
    if c >= d and winner.lower() == 'a':
        score += 1
        print(f"You're right to choose 'A'  Current score {score}")

    elif c <= d and winner.lower() == 'b':
        score += 1
        print(f"You're right to choose 'B'  Current score {score}")
    else:
        return 0


check_followers()
d = True

while d:

    random_dica()
    A = name
    print(f"Compare 'A': {name} , a {description} , from {country}.")

    print(vs)

    random_dica()
    B = name
    if A == B:
        random_dica()
        print(f"Aginst 'B': {name} , a {description} , from {country}.")
    else:
        print(f"Aginst 'B': {name} , a {description} , from {country}.")
    check_followers()
    winner = input("Who has more followers ? 'A' or 'B' :")

    if check_followers() == 0:
        print(f"Sorry, that's wrong . Final score {score}")
        d = False
