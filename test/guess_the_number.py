import random
sec= random.randint(1,50)
lives=5

print("Welcome to the number guessing game.")
print("Guess a number between 1-50.")

while lives>0:
    guess=int(input("\nEnter your guess: "))

    if guess==sec:
        print("Congratulations, your guess is correct.")
        break
    else:
        lives=lives-1

    dif=sec-guess
    if dif<=5:
        print("Hot!You are very close.")
    elif dif<=15:
        print("Warm!You are getting closer.")
    elif dif<=25:
        print("Cold!You are a bit far.")
    else:
        print("Ice cold!You are WAYY off.")

    print("Remaining lives:", end="")
    for i in range(lives):
        print("*", end="")

if lives==0:
    print("Game over, the secret number was", sec)