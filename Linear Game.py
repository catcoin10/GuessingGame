# This program runs in O(b) time.
# This variation was achieved by changing just one variable.

from random import randint

global secret
max = 10**10
# oracle
secret = randint(1, max) # get a random number

def oracle(guess):
    if guess == secret:
        return 0
    if guess > secret:
        return 1
    if guess < secret:
        return -1

print(secret)
# guesser
guesses = 0
lowbound = 1
upbound = max
while True:
    r = randint(lowbound, upbound)
    guess = oracle(r)
    print("Guessing number " + str(r) + " with upper bound " + str(upbound) + " and lower bound " + str(lowbound))
    if guess == 0: break
    if guess == 1: upbound = r-1
    if guess ==-1: lowbound = r+1
    guesses += 1
print(guesses)
