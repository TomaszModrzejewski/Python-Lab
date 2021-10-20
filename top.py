from typing import Any


dice = {}
for i in range(1, 7):
    for j in range(1, 7):
        dice.setdefault(i+j, set())
        dice[i+j].add((i, j))
print(dice[7])
