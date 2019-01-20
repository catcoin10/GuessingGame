# This program runs in O(b) time.
# This variation was achieved by changing just one variable.

from random import randint

def oracle(guess):
    if guess == secret:
        return 0
    if guess > secret:
        return 1
    if guess < secret:
        return -1

class tiresias:
    max = 5
    secret = randint(1, max)
    def oracle(guess):
        if guess == tiresias.secret:
            return 0
        if guess > tiresias.secret:
            return 1
        if guess < tiresias.secret:
            return -1

class odysseus:
    guesses = 0
    lowbound = tiresias.max # the only part that Tiresias lets you see without going to Tartarus.
    def talk_to_tiresias(): # interrogate Tiresias to make him tell me what the secret number is saying.
        lowbound = 1
        upbound = tiresias.max
        while True:
            r = randint(lowbound, upbound)
            guess = tiresias.oracle(r)
            if guess == 0:  break
            if guess == 1:  upbound = r - 1
            if guess== -1:  lowbound = r + 1
            guesses += 1

odysseus.talk_to_tiresias()
