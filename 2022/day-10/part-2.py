import pandas as pd
import numpy as np

with open("2022/day-10/input.txt", "r") as f:
    lines = f.readlines()
    lines = [l.strip().split(' ') for l in lines]

cycles = {"noop": 1, "addx" : 2}

df = pd.DataFrame(lines, columns=["add_cycles", "v"]).replace(cycles).fillna(0).astype(int)
df["cycle"] = df["add_cycles"].cumsum()
df["v_cumsum"] = 1 + df["v"].cumsum()

sprite = [0, 1, 2]
all_rows = []
for i in range(6):
    row = ''
    sprite = [0, 1, 2]
    for j in range(0, 40):
        if j in sprite:
            row += '#'
        else:
            row += '.'
        if (i*40)+j+1 in list(df["cycle"]):
            X = df.loc[df["cycle"] == (i*40)+j+1, "v_cumsum"].values[0]
            sprite = [X-1, X, X+1]
    print(row)
