base_path = "/Users/sarathiringer/DEV/projects/AdventOfCode/2023/day-1/"

with open(base_path + "input.txt", "r") as f:
    lines = f.readlines()

sum_of_numbers = 0

words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

digits_as_words = dict(zip(words, digits))

for line in lines:
    digit = ""
    stop = False
    line = line.strip()
    word = ""
    for l in line:
        if stop:
            break
        elif l.isnumeric():
            digit += l
            stop = True
        elif not l.isnumeric():
            word += l
            is_word_list = [s in word for s in words]
            if any(is_word_list):
                is_word_index = is_word_list.index(True)
                digit += digits[is_word_index]
                word = ""
                stop = True
    stop = False
    for l in line[::-1]:
        if stop:
            break
        elif l.isnumeric():
            digit += l
            stop = True
        elif not l.isnumeric():
            word += l
            is_word_list = [s in word[::-1] for s in words]
            if any(is_word_list):
                is_word_index = is_word_list.index(True)
                digit += digits[is_word_index]
                word = ""
                stop = True
    if stop == False:
        print(f"No numbers in this input: {line}")
    sum_of_numbers += int(digit)

print(sum_of_numbers)
