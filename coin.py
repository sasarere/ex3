import random

print("Who are you?")
name = input("> ")
print(f"Hello, {name}!")

print("Tossing a coin...")

results = [random.choice(["Heads","Tails"]) for _ in range(3)]

for i, res in enumerate(results, 1):
  print(f"Round {i}: {res}")

heads_count = results.count("Heads")
tails_count = results.count("Tails")

print(f"Heads: {heads_count}, Tails: {tails_count}")

if heads_count > tails_count:
  print("You won")
else:
  print("You lost")
