# a guessing name
import random as rand


maxi = 20
correct = rand.randint(1,maxi)
cnt = 0

while True:
    cnt += 1
    guess = int(input("What is your guess? "))
    if guess < correct:
        print("Your guess is too low")
    elif guess > correct:
        print("Your guess is too high")
    else:
        break

print(f"Congratulations! You guessed correctly in {cnt} guesses.")
