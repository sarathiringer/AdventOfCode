import string

# Get input
with open("2022/day-3/input.txt", "r") as f:
    lines = f.readlines()

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
for line in lines:
    split_at = int(len(line)/2)
    first, second = line[:split_at], line[split_at:]
    shared_items = list(set(first) & set(second))
    for i in shared_items:
        total_priority += priorities[i]

print("The total priority is", total_priority)
