import sys, random

Ran_num = random.randint(1,20)
count = 1

print("I am thinking of a number between 1 and 20.")

def engine(Ran_num, count):

    while True:
        guess = int(input("Take a guess  > "))

        if guess > Ran_num:
            print("Wrong! Your guess is higher. Try a lower number.")
            count += 1
            continue

        elif guess < Ran_num:
            print("Wrong! Your guess is lower. Try a higher number.")
            count += 1
            continue

        else:
            print(f"Correct! The answer was {Ran_num}")
            print(f"You guessed it in {count} tries.")
            sys.exit()

engine(Ran_num, count)
