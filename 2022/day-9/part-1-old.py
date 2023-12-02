import pandas as pd
import numpy as np

with open("2022/day-9/input.txt", "r") as f:
    lines = f.readlines()
    lines = [l.strip().split(' ') for l in lines]

df = pd.DataFrame(lines)
df[1] = df[1].astype(int)
grid_size = df.groupby([0]).sum().max().values[0]*2
grid = np.zeros((grid_size, grid_size))

where = (int(grid_size/2), int(grid_size/2))
grid[where] = 1
changes = {
    'L': lambda x: (x[0], x[1]-1), 
    'R': lambda x: (x[0], x[1]+1),
    'U': lambda x: (x[0]-1, x[1]),
    'D': lambda x: (x[0]+1, x[1])
}
corners = 0
previous_direction = None
new_places = 0
for direction, steps in lines:
    for i in range(1, int(steps)+1):
        new_where = changes[direction](where)
        grid[new_where] = 1
        if grid[where] > 0 and not grid[where] == 2:
            new_places += 1
        grid[where] = 2
        where = new_where
    if previous_direction:
        corners += 1
    previous_direction = direction

print(new_places-corners)