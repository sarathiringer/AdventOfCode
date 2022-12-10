import numpy as np
from scipy.spatial import distance

with open("2022/day-9/input.txt", "r") as f:
    lines = f.readlines()
    lines = [l.strip().split(' ') for l in lines]
    lines = [[i, int(j)] for i, j in lines]

changes = {
    'L': lambda x: (x[0], x[1]-1), 
    'R': lambda x: (x[0], x[1]+1),
    'U': lambda x: (x[0]-1, x[1]),
    'D': lambda x: (x[0]+1, x[1])
}

head = (0, 0)
tail = (0, 0)
tail_visits = []

previous_direction = None
for line in lines:
    direction = line[0]
    steps = line[1]
    for step in range(steps):
        head = changes[direction](head)
        if distance.euclidean(head, tail) < 1.5:
            tail_visits.append(tail)
            continue
        else:
            possible_new_tail = [v(head) for k, v in changes.items()]
            tail = possible_new_tail[np.argmin([distance.euclidean(tail, t) for t in possible_new_tail])]
            tail_visits.append(tail)

print(f"The tail have visited {len(set(tail_visits))} spots.")