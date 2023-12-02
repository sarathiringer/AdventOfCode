with open("input-1.txt", "r") as f:
    lines = f.readlines()

calories = []
cal = 0
for line in lines:
    line = line.strip()
    if line:
        cal += int(line)
    else:
        calories.append(cal)
        cal = 0

# Part 1
print("The elf carrying the most is carrying", max(calories), "calories.")

# Part 2
calories.sort()
print("The top three elves are carrying", sum(calories[-3:]), "calories worth of snacks. Good job elves!")
