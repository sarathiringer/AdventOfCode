import string
import numpy as np

# Get input
with open("2022/day-3/input.txt", "r") as f:
    lines = f.readlines()
    lines = np.array(lines).reshape((int(len(lines)/3)), 3)

# Map items to their priorities
letters = string.ascii_lowercase + string.ascii_uppercase
priorities = dict(
    zip(
        letters,
        [i for i, l in enumerate(letters, 1)]
    )
)

# Sum up the priority
total_priority = 0
for group in lines:
    group = [g.strip() for g in group]
    badge = list(set(group[0]) & set(group[1]) & set(group[2]))
    total_priority += priorities[badge[0]]

print("The total priority of badges is", total_priority)
