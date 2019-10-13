# Die Hilfsfunktion name_to_number() funzt noch nicht richtig. Output: None.
# Außerdem fehlt noch das Unentschieden! (Spock-Spock etc.)

import random

rock = 0
Spock = 1
paper = 2
lizard = 3
scissors = 4

c = random.randrange(0,5)

def rpsls(h):
    print("You:", number_to_name(h), "; Computer:", number_to_name(c))
    if (h-c)%5 < 3:
        print("Success! You win!")
    else:
        print("Damn. You lose.")


def number_to_name(x):
    if x == 0:
        print("rock")
    elif x == 1:
        print("Spock")
    elif x == 2:
        print("paper")
    elif x == 3:
        print("lizard")
    else:
        print("scissors")






rpsls(rock)
rpsls(scissors)
rpsls(Spock)
