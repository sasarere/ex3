import randam

print("Tossing a coin...")

results = [random.choice(["Heads","Tails"]) for _ in range(3)]

for i, res in enumerate(results, 1):
  print(f"Round {i}: {res}")

heads_count = results.count("Head")
tails_count = results.count("Tails")

print(f"Heads: {heads_count}, Tails: {tails_count}")
