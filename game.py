import random

print("🎮 Guess My Number Game!")
level = input("1️=Easy, 2️=Medium, 3️=Hard: ")

ranges = {
    "1": (1, 10),
    "2": (11, 30),
    "3": (31, 60)
}

low, high = ranges.get(level, (1, 10))
secret = random.randint(low, high)

print(f"Guess a number between {low} and {high}!")
tries = 0

while True:
    try:
        guess = int(input("Enter your guess:"))
    except ValueError:
        print("⚠️ Enter a valid number!")
        continue

    if guess < low or guess > high:
        print(f"🚫 Guess must be between {low} and {high}.")
        continue

    tries += 1

    if guess == secret:
        print(f"🎉 Correct! You guessed it in {tries} tries!")
        break
    elif guess < secret:
        print("Too low! Go higher.")
    else:
        print(("Too high! Go lower."))

        # Fun hint
    if abs(guess - secret) < 5:
        print("Getting warmer! 🔥")
    else:
        print("Freezing cold! ❄️")

print("👏 Good game!")



