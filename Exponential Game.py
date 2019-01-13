# Guess with exponential (O(2^b) time) when b is the number of bits.
# Time is O(n) where n is the maximum number.
from random import randint

global secret
max = 10**3 # we cannot have the max too low
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
    if guess == 1: upbound = upbound-1
    if guess ==-1: lowbound = lowbound+1
    guesses += 1
print(guesses)
