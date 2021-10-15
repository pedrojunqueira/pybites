from itertools import combinations
import random

notes = ["5","10","20","50","100"]
coins = ["5c", "10c", "20c", "50c", "1", "2"]

note_combs = list(combinations(notes,2))
coin_combs = list(combinations(coins,5))


possibilities = []

for note in note_combs:
    for coin in coin_combs:
        possibilities.append((note, coin))

for i, possibility in enumerate(possibilities):
    print(f"{i+1}: {possibility}")