# Get input
with open("2022/day-4/input.txt", "r") as f:
    lines = f.readlines()

count = 0
for line in lines:
    first, second = line.split(',')
    first_first, first_second = first.split('-')
    second_first, second_second = second.split('-')
    first_first, first_second, second_first, second_second = [
        int(i) for i in [first_first, first_second, second_first, second_second]
    ]
    if not (first_first > second_second or first_second < second_first):
        count += 1

print("There are", count, "assignment pairs which overlap each other.")




