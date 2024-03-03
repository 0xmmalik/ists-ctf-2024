import random

print("Welcome to the Number Guessing Game!")
m = random.Random()
correct = m.getrandbits(128)
guess = int(input("I'm thinking of a 128-bit number. What's my number? "))
while guess != correct:
    print("That's not right. My number was " + str(correct) + ".")
    correct = m.getrandbits(128)
    guess = int(input("I'm thinking of a 128-bit number. What's my number? "))
if guess == correct: print("That's correct! Here's a flag for you, you guessing whiz: ISTS{w3_g07_c0wz}")