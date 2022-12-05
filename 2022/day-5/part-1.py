# Get stacks
with open("2022/day-5/input-1.txt", "r") as f:
    lines = f.readlines()
    lines.reverse()
    lines = lines[1:]

all_lines = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
]
for i, line in enumerate(lines):
    my_list = []
    for j, k in enumerate(range(0, len(line)-3, 4)):
        all_lines[j].append(line[k+1])

all_lines = [[j for j in i if j.isalpha()] for i in all_lines]

# Get instructions
with open("2022/day-5/input-2.txt", "r") as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]

for line in lines:
    line = line.split()
    digits = line[1], line[3], line[5]
    digits = [int(d) for d in digits]
    number, fr, to = digits
    for i in range(1, number+1):
        to_move = all_lines[fr-1].pop()
        all_lines[to-1].append(to_move)

top = []
for line in all_lines:
    top.append(line.pop())

print("The crades on top of the stacks are", ''.join(top))