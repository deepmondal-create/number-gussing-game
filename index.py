import random

num = random.randint(1, 100)
times = 0

while True:
    try:
        user_Num = int(input("Guess a number between 1 and 100? "))
    except ValueError:
        print("Sirf number likho!")
        continue

    times = times + 1

    if user_Num == num:
        print("Congratulations! You guessed it right in", times, "attempts")
        break
    elif user_Num > num:
        print("Your number is too high!")
    else:
        print("Your number is too low!")
        