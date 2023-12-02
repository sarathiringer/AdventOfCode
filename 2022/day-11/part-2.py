import numpy as np
import math

with open("2022/day-11/input.txt", "r") as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]
    lines = [lines[i: i+7] for i in range(0, len(lines), 7)]


class Monkey():
    def __init__(self, nr, items, operation, test):
        #op = {
        #    "*": np.multiply,
        #    "+": np.add,
        #    "-": np.subtract,
        #    "/": np.divide
        #}
        self.nr = nr
        self.items = items
        self.op = operation[0]
        self.operation_2 = operation[1]
        self.divide_by = test[0]
        self.if_true_throw_to = test[1]
        self.if_false_throw_to = test [2]
        self.number_of_inspections = 0

    def inspect(self):
        item = self.items.pop(0)
        new = None
        if self.op == "*":
            other = item if self.operation_2 == 'old' else np.log(int(self.operation_2))
            new = item + other
        elif self.op == "+":
            new = np.log(np.exp(item) + int(self.operation_2))
        #if type(new) != int:
        #    print(type(new))
        self.new = new

    def test_item(self):
        #self.new = math.floor(self.new / 3)
        if (self.new - self.divide_by) == int((self.new - self.divide_by)):
            pass_to = self.if_true_throw_to
        else:
            pass_to = self.if_false_throw_to
        
        return self.new, pass_to


monkeys = []

for line in lines:
    nr = int(line[0][-2])
    items = [np.log(int(i)) for i in line[1][15:].split(',')]
    operation = (line[2][21], line[2][23:])
    test = (np.log(int(line[3][19:])), int(line[4][24:]), int(line[5][26:]))
    monkey = Monkey(nr, items, operation, test)
    monkeys.append(monkey)

for round in range(20):
    for monkey in monkeys:
        while monkey.items:
            print(monkey.items)
            monkey.inspect()
            monkey.number_of_inspections += 1
            item, throws_to = monkey.test_item()
            monkeys[throws_to].items.append(item)

inspections = [m.number_of_inspections for m in monkeys]
inspections.sort()
print(inspections)
print(inspections[-1], inspections[-2])
print(inspections[-1]*inspections[-2])

# 52166
# 52013
# 2713310158
