with open("2022/day-6/input.txt", "r") as f:
    line = f.readline()

# Part 1: 4
# Part 2: 14
window_size = 4

for i in range(len(line)):
    window = line[i:i+window_size]
    if len(set(window)) == window_size:
        print(i+window_size)
        break