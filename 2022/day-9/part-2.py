import numpy as np
from scipy.spatial import distance

with open("2022/day-9/input.txt", "r") as f:
    lines = f.readlines()
    lines = [l.strip().split(' ') for l in lines]
    lines = [[i, int(j)] for i, j in lines]

changes = {
    'L': lambda x: (x[0]-1, x[1]), 
    'R': lambda x: (x[0]+1, x[1]),
    'U': lambda x: (x[0], x[1]+1),
    'D': lambda x: (x[0], x[1]-1)
}

rope = [
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
]
tail_visits = []

previous_direction = None
for line in lines:
    direction = line[0]
    steps = line[1]
    for step in range(steps):
        rope[0] = changes[direction](rope[0])
        for i in range(1, len(rope)):
            if distance.euclidean(rope[i-1], rope[i]) < 1.5:
                continue
            else:
                possible_new_place = [v(rope[i-1]) for k, v in changes.items()] # Why use these
                distances = [distance.euclidean(rope[i], t) for t in possible_new_place]
                distances.sort()
                if distances[0] == distances[1]:
                    rope[i] = tuple((np.array(rope[i])+np.array(rope[i-1]))/2)
                else:
                    rope[i] = possible_new_place[np.argmin([distance.euclidean(rope[i], t) for t in possible_new_place])]
        
        if rope[-1] not in tail_visits:
            tail_visits.append(rope[-1])

print(f"The tail have visited {len(tail_visits)} spots.")
