import sys, random

def control_int():
    while True:
        try:
            guess = int(input("Take a guess > "))
            return guess
        except:
            print("THAT IS NOT A NUMBER! Try again.")
            continue


def engine(Ran_num, count):
    while True:
        guess = control_int()
        if guess > Ran_num:
            print("Wrong! Your number is higher. Try a lower number.")
            count += 1
            continue

        elif guess < Ran_num:
            print("Wrong! Your number is lower. Try a higher number.")
            count += 1
            continue

        else:
            print(f"Correct! The answer was {Ran_num}")
            print(f"You guessed it in {count} tries.")
            sys.exit()


print("I am thinking of a number between 1 and 20.")
Ran_num = random.randint(1,20)
count = 1

engine(Ran_num, count)
